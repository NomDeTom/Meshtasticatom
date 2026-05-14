import threading
import unittest

from lib.interface_close import InterfaceCloseTimeout, close_interface


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


if __name__ == "__main__":
    unittest.main()
