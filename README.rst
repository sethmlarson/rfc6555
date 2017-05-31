rfc6555
=======

.. image:: https://img.shields.io/travis/SethMichaelLarson/rfc6555/master.svg?style=flat-square
    :target: https://travis-ci.org/SethMichaelLarson/rfc6555
.. image:: https://img.shields.io/appveyor/ci/SethMichaelLarson/rfc6555/master.svg?style=flat-square
    :target: https://ci.appveyor.com/project/SethMichaelLarson/rfc6555
.. image:: https://img.shields.io/pypi/v/rfc6555.svg?style=flat-square
    :target: https://pypi.python.org/pypi/rfc6555
.. image:: https://img.shields.io/badge/say-thanks-ff69b4.svg?style=flat-square
    :target: https://saythanks.io/to/SethMichaelLarson

Python implementation of the Happy Eyeballs Algorithm described in `RFC 6555 <https://tools.ietf.org/html/rfc6555>`_.
Provided with a single file and dead-simple API to allow easy vendoring
and integration into other projects.

Abstract
--------

When a server's IPv4 path and protocol are working, but the server's
IPv6 path and protocol are not working, a dual-stack client
application experiences significant connection delay compared to an
IPv4-only client.  This is undesirable because it causes the dual-
stack client to have a worse user experience.  This document
specifies requirements for algorithms that reduce this user-visible
delay and provides an algorithm.

- `Abstract from RFC 6555 <https://tools.ietf.org/html/rfc6555>`_

Installation
------------

``$ python -m pip install rfc6555``

Usage
-----

The main API for the ``rfc6555`` module is via ``rfc6555.create_connection()`` which
functions identically to ``socket.create_connection()`` with the same arguments.
This function will automatically fall back on a ``socket.create_connection()`` call if
RFC 6555 is not supported (for instance on platforms not capable of IPv6) or if
RFC 6555 is disabled via setting ``rfc6555.RFC6555_ENABLED`` equal to ``False``.

 .. code-block:: python
 
    import rfc6555
    sock = rfc6555.create_connection(('www.google.com', 80), timeout=10, source_address=('::1', 0))

    # This will disable the Happy Eyeballs algorithm for future
    # calls to create_connection()
    rfc6555.RFC6555_ENABLED = False

Support
-------

This module supports Python 2.6 or newer and supports all major platforms.
Additionally if you have ``selectors2>=2.0.0`` installed this module will
also support Jython in addition to CPython.
