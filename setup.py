import os
import re
from setuptools import setup

# Get the version (borrowed from SQLAlchemy)
base_path = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(base_path, 'rfc6555.py')) as f:
    VERSION = re.compile(r'.*__version__ = \'(.*?)\'', re.S).match(f.read()).group(1)

with open(os.path.join(base_path, 'README.rst')) as f:
    long_description = f.read()

with open(os.path.join(base_path, 'CHANGES.rst')) as f:
    changes = f.read()

if __name__ == '__main__':
    setup(name='rfc6555',
          description='Python implementation of the Happy Eyeballs Algorithm described in RFC 6555.',
          long_description=long_description + '\n\n' + changes,
          license='Apache-2.0',
          url='https://www.github.com/SethMichaelLarson/rfc6555',
          version=VERSION,
          author='Seth Michael Larson',
          author_email='sethmichaellarson@protonmail.com',
          maintainer='Seth Michael Larson',
          maintainer_email='sethmichaellarson@protonmail.com',
          install_requires=['selectors2'],
          py_modules=['rfc6555'],
          zip_safe=False,
          classifiers=['Intended Audience :: Developers',
                       'License :: OSI Approved :: Apache Software License',
                       'Natural Language :: English',
                       'Operating System :: OS Independent',
                       'Programming Language :: Python :: 2',
                       'Programming Language :: Python :: 2.6',
                       'Programming Language :: Python :: 2.7',
                       'Programming Language :: Python :: 3',
                       'Programming Language :: Python :: 3.3',
                       'Programming Language :: Python :: 3.4',
                       'Programming Language :: Python :: 3.5',
                       'Programming Language :: Python :: 3.6',
                       'Topic :: Internet',
                       'Topic :: System :: Networking'])
