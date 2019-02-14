rfc6555
=======

.. image:: https://img.shields.io/travis/SethMichaelLarson/rfc6555/master.svg?style=flat-square
    :target: https://travis-ci.org/SethMichaelLarson/rfc6555

.. image:: https://img.shields.io/appveyor/ci/SethMichaelLarson/rfc6555/master.svg?style=flat-square
    :target: https://ci.appveyor.com/project/SethMichaelLarson/rfc6555

.. image:: https://img.shields.io/codecov/c/github/SethMichaelLarson/rfc6555/master.svg?style=flat-square
    :target: https://codecov.io/gh/SethMichaelLarson/rfc6555

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

~ `Abstract from RFC 6555 <https://tools.ietf.org/html/rfc6555>`_

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

This module supports Python 2.6 or newer and supports all major platforms.
Additionally if you have ``selectors2>=2.0.0`` installed this module will
also support Jython in addition to CPython.

License
-------

The ``rfc6555`` package is released under the ``Apache-2.0`` license.

See `full license text in LICENSE file <https://github.com/SethMichaelLarson/rfc6555/blob/master/LICENSE>`_ for more information.

 .. code-block::

                Copyright 2017 Seth Michael Larson
  
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at
  
            http://www.apache.org/licenses/LICENSE-2.0
  
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.

Alternatives
------------

For asyncio support check out https://pypi.org/project/async-stagger/
