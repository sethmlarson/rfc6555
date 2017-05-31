import mock
import pytest
import socket
import rfc6555
from .test_utils import requires_network


class _BasicCreateConnectionTests(object):
    @requires_network
    def test_create_connection_google(self):
        sock = rfc6555.create_connection(('www.google.com', 80))

    @pytest.mark.parametrize('timeout', [None, 5.0])
    def test_create_connection_has_proper_timeout(self, timeout):
        sock = rfc6555.create_connection(('www.google.com', 80), timeout=timeout)

        assert sock.gettimeout() == timeout

    def test_create_connection_with_source_address_calls_bind(self):
        sock = mock.Mock()
        with mock.patch('socket.socket') as fake_socket:
            fake_socket.return_value = sock

            sock.getsockopt.return_value = 0
            sock.connect_ex.return_value = 0
            sock.gettimeout.return_value = None

            try:
                rfc6555.create_connection(('::1', 0), source_address=('::1', 123))
            except Exception:
                pass

            sock.bind.assert_called_with(('::1', 123))

    def test_getaddr_info_empty_list(self):
        with mock.patch('socket.getaddrinfo') as fake_getaddrinfo:
            fake_getaddrinfo.return_value = []

            with pytest.raises(socket.error):
                rfc6555.create_connection(('::1', 0))

    @requires_network
    def test_create_connection_cached_value(self):
        sock = rfc6555.create_connection(('www.google.com', 80))
        sock2 = rfc6555.create_connection(('www.google.com', 80))


class TestCreateConnectionTestRFC6555Default(_BasicCreateConnectionTests):
    pass


class TestCreateConnectionTestRFC6555Enabled(_BasicCreateConnectionTests):
    def setup_method(self, test_method):
        rfc6555.RFC6555_ENABLED = True


class TestCreateConnectionTestRFC6555Disabled(_BasicCreateConnectionTests):
    def setup_method(self, test_method):
        rfc6555.RFC6555_ENABLED = False
