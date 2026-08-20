import errno
import importlib.util
import os
import sys
import threading
import types
import unittest

from lib.interface_close import InterfaceCloseTimeout, close_interface


class Graph:
    pass


def load_interactive_module():
    """Load interactive.py with a GUI stub without poisoning lib.interactive."""
    module_name = "_interactive_shutdown_test"
    gui_stub = types.ModuleType("lib.gui")
    gui_stub.Graph = Graph
    gui_stub.gen_scenario = lambda conf: []
    previous_gui = sys.modules.get("lib.gui")
    sys.modules["lib.gui"] = gui_stub
    module_path = os.path.join(os.path.dirname(__file__), "..", "lib", "interactive.py")
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
        return module
    finally:
        sys.modules.pop(module_name, None)
        if previous_gui is None:
            del sys.modules["lib.gui"]
        else:
            sys.modules["lib.gui"] = previous_gui


interactive = load_interactive_module()
InteractiveSim = interactive.InteractiveSim


class TestInteractiveInterfaceClose(unittest.TestCase):
    def test_close_interface_calls_close(self):
        class Interface:
            closed = False

            def close(self):
                self.closed = True

        iface = Interface()

        close_interface(iface, timeout=0.5)

        self.assertTrue(iface.closed)

    def test_close_interface_preserves_close_errors(self):
        class Interface:
            def close(self):
                raise OSError("socket already gone")

        with self.assertRaisesRegex(OSError, "socket already gone"):
            close_interface(Interface(), timeout=0.5)

    def test_close_interface_times_out_on_hung_reader_thread(self):
        class Interface:
            def __init__(self):
                self.started = threading.Event()
                self.release = threading.Event()

            def close(self):
                self.started.set()
                self.release.wait(5)

        iface = Interface()

        try:
            with self.assertRaisesRegex(InterfaceCloseTimeout, "0.01s"):
                close_interface(iface, timeout=0.01)
            self.assertTrue(iface.started.is_set())
        finally:
            iface.release.set()


class TestInteractiveShutdown(unittest.TestCase):
    def make_sim(self, nodes, container=None):
        sim = object.__new__(InteractiveSim)
        sim.nodes = nodes
        sim.docker = container is not None
        sim.container = container
        sim.forwardToClient = False
        sim.forwardSocket = None
        sim.clientSocket = None
        sim.wantExit = False
        return sim

    def test_close_nodes_ignores_already_closed_node_socket(self):
        class LocalNode:
            def exitSimulator(self):
                raise OSError(errno.EBADF, "Bad file descriptor")

        class Interface:
            localNode = LocalNode()
            close_attempted = False

            def close(self):
                self.close_attempted = True
                raise OSError(errno.EBADF, "Bad file descriptor")

        iface = Interface()

        node = type("Node", (), {})()
        node.nodeid = 0
        node.iface = iface
        sim = self.make_sim([node])

        sim.close_nodes()

        self.assertIsNone(node.iface)
        self.assertTrue(iface.close_attempted)

    def test_close_nodes_preserves_unexpected_exit_errors(self):
        class LocalNode:
            def exitSimulator(self):
                raise OSError(errno.EIO, "device IO failed")

        class Interface:
            localNode = LocalNode()

        class Node:
            nodeid = 0
            iface = Interface()

        sim = self.make_sim([Node()])

        with self.assertRaisesRegex(OSError, "device IO failed"):
            sim.close_nodes()

    def test_close_nodes_ignores_auto_removed_docker_container(self):
        class Interface:
            class localNode:
                @staticmethod
                def exitSimulator():
                    pass

            def close(self):
                pass

        class Node:
            nodeid = 0
            iface = Interface()

        class DockerNotFound(Exception):
            status_code = 404

        class Container:
            def stop(self):
                raise DockerNotFound("No such container")

        sim = self.make_sim([Node()], container=Container())

        sim.close_nodes()

        self.assertIsNone(sim.nodes[0].iface)

    def test_stop_container_keeps_unexpected_docker_errors_visible(self):
        class Container:
            def stop(self):
                raise RuntimeError("docker daemon unavailable")

        sim = self.make_sim([], container=Container())

        with self.assertRaisesRegex(RuntimeError, "docker daemon unavailable"):
            sim.stop_container()


if __name__ == "__main__":
    unittest.main()


class TestNodeStartCommands(unittest.TestCase):
    """Two meshtasticd processes sharing a -d directory read and write each other's state."""

    class Node:
        def __init__(self, nodeid):
            self.nodeid = nodeid
            self.hwId = 0x1000 + nodeid
            self.TCPPort = 4403 + nodeid

    def commands(self, log=False):
        node_start_command = interactive.node_start_command

        nodes = [self.Node(i) for i in range(6)]
        return [
            node_start_command(
                n, remove_config=True, log_path=f"/home/out_{n.nodeid}.log" if log else None
            )
            for n in nodes
        ]

    def data_dirs(self, commands):
        return [c.split("-d ")[1].split()[0] for c in commands]

    def test_every_node_gets_its_own_data_directory(self):
        for log in (False, True):
            with self.subTest(log_path=log):
                dirs = self.data_dirs(self.commands(log))
                self.assertEqual(len(set(dirs)), 6, dirs)

    def test_the_data_directory_names_the_node_it_belongs_to(self):
        for nodeid, directory in enumerate(self.data_dirs(self.commands())):
            self.assertEqual(directory, f"/home/node{nodeid}")

    def test_every_node_gets_its_own_port_and_hardware_id(self):
        commands = self.commands()
        ports = [c.split("-p ")[1].split()[0] for c in commands]
        hw_ids = [c.split("-h ")[1].split()[0] for c in commands]
        self.assertEqual(len(set(ports)), 6)
        self.assertEqual(len(set(hw_ids)), 6)

    def test_the_daemon_image_is_pinned_to_a_tag(self):
        image = interactive.DEVICE_SIM_DOCKER_IMAGE
        self.assertIn(":", image)
        self.assertFalse(image.endswith(":latest"))
