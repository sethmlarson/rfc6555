Happy Eyeballs in Python (RFC 6555)
===================================

.. image:: https://github.com/sethmlarson/rfc6555/actions/workflows/ci.yml/badge.svg
    :target: https://github.com/sethmlarson/rfc6555/actions/workflows/ci.yml

.. image:: https://codecov.io/gh/sethmlarson/rfc6555/branch/master/graph/badge.svg?token=Xn7oQWErjc
    :target: https://codecov.io/gh/sethmlarson/rfc6555    

.. image:: https://img.shields.io/pypi/v/rfc6555.svg?style=flat-square
    :target: https://pypi.python.org/pypi/rfc6555

Synchronous Python implementation of the Happy Eyeballs Algorithm described in `RFC 6555 <https://tools.ietf.org/html/rfc6555>`_.
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

Installation
------------

 .. code-block:: bash

    $ python -m pip install rfc6555

Usage
-----

The main API for the ``rfc6555`` module is via ``rfc6555.create_connection()`` which
functions identically to ``socket.create_connection()`` with the same arguments.
This function will automatically fall back on a ``socket.create_connection()`` call if
RFC 6555 is not supported (for instance on platforms not capable of IPv6) or if
RFC 6555 is disabled via setting ``rfc6555.RFC6555_ENABLED`` equal to ``False``.

**IMPORTANT:** Caching is **NOT** thread-safe by default. If you require thread-safe caching
one should create their own implementation of ``rfc6555._RFC6555CacheManager`` object that
is thread-safe and assign an instance to ``rfc6555.cache``.

 .. code-block:: python
 
  import rfc6555
  sock = rfc6555.create_connection(('www.google.com', 80), timeout=10, source_address=('::1', 0))

  # This will disable the Happy Eyeballs algorithm for future
  # calls to create_connection()
  rfc6555.RFC6555_ENABLED = False
  
  # Use this to set a different duration for cache entries.
  rfc6555.cache.validity_duration = 10  # 10 second validity time.

  # Use this to disable caching.
  rfc6555.cache.enabled = False

Support
-------

This module supports Python 2.7 or newer and supports all major platforms.
Additionally if you have ``selectors2>=2.0.0`` installed this module will
also support Jython in addition to CPython.

License
-------

The ``rfc6555`` package is released under the ``Apache-2.0`` license.

See `full license text in LICENSE file <https://github.com/sethmlarson/rfc6555/blob/master/LICENSE>`_ for more information.
