import pytest
import socket


def _check_network():
    sock = None
    try:
        sock = socket.create_connection(('www.google.com', 80))
        sock.close()
        return True
    except Exception:
        if sock:
            sock.close()
        return False


requires_network = pytest.mark.skipif(not _check_network(), reason='This test requires a network connection.')
