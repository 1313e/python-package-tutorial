# -*- coding: utf-8 -*-

"""
TestPy Setup
===========
Contains the setup script required for installing the *TestPy* package.
This can be ran directly by using::

    pip install .

or anything equivalent.

"""


# %% IMPORTS
# Future imports
from __future__ import absolute_import, with_statement

# Built-in imports
from codecs import open

# Package imports
from setuptools import find_packages, setup


# %% SETUP DEFINITION
# Get the long description from the README file
with open('README.rst', 'r') as f:
    long_description = f.read()

# Get the requirements list
with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

# Get the version
exec(open('testpy/__version__.py', 'r').read())

# Setup function declaration
# See https://setuptools.readthedocs.io/en/latest/setuptools.html
setup(name='testpy-cas',    # Registered name of package (e.g., on PyPI)
      version=version,      # Version of this package
      author="Ellert van der Velden",
      author_email="evandervelden@swin.edu.au",
      maintainer="1313e",   # PyPI username of maintainer(s)
      description=("TestPy: A tutorial on how to build a Python package"),
      long_description=long_description,        # Use the README description
      license='MIT',    # License of this package
      # List of classifiers (https://pypi.org/pypi?%3Aaction=list_classifiers)
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: MacOS',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: Unix',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Topic :: Software Development'
          ],
      keywords=('testpy'),  # List of keywords
      # String containing the Python version requirements
      python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',
      packages=find_packages(),
      # Registered namespace vs. local directory
      package_dir={'testpy': "testpy"},
      include_package_data=True,        # Include non-Python files
      install_requires=requirements,    # Parse in list of requirements
      zip_safe=False,                   # Do not zip the installed package
      )
