import threading


IFACE_CLOSE_TIMEOUT_SECONDS = 5


class InterfaceCloseTimeout(TimeoutError):
    """Raised when a Meshtastic TCP interface does not finish closing."""


def close_interface(iface, timeout=IFACE_CLOSE_TIMEOUT_SECONDS):
    """Close a Meshtastic interface without letting its reader thread hang forever.

    A native setup can block in TCPInterface.close(), so this closes in a daemon thread.
    """
    if iface is None:
        return

    errors = []

    def run_close():
        try:
            iface.close()
        except Exception as ex:
            errors.append(ex)

    close_thread = threading.Thread(target=run_close, daemon=True)
    close_thread.start()
    close_thread.join(timeout)
    if close_thread.is_alive():
        raise InterfaceCloseTimeout(f"interface close did not finish within {timeout:g}s")
    if errors:
        raise errors[0]
