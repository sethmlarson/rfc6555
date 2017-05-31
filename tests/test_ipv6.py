import socket
import mock
import rfc6555


def test_ipv6_available():
    assert rfc6555._detect_ipv6()


def test_ipv6_not_available_socket_has_ipv6_false():
    old_has_ipv6 = socket.has_ipv6
    socket.has_ipv6 = False
    assert not rfc6555._detect_ipv6()
    socket.has_ipv6 = old_has_ipv6


def test_ipv6_not_available_socket_exception_on_init():
    with mock.patch('socket.socket') as fake_socket:
        fake_socket.side_effect = OSError

        assert not rfc6555._detect_ipv6()


def test_ipv6_not_available_socket_exception_on_bind():
    sock = mock.Mock()
    with mock.patch('socket.socket') as fake_socket:
        fake_socket.return_value = sock
        sock.bind.side_effect = OSError

        assert not rfc6555._detect_ipv6()


def test_ipv6_not_available_socket_AF_INET6_not_defined():
    old_AF_INET6 = socket.AF_INET6
    try:
        delattr(socket, 'AF_INET6')
        assert not rfc6555._detect_ipv6()
    finally:
        socket.AF_INET6 = old_AF_INET6
