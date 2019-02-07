# -*- coding: utf-8 -*-

"""
TuPy
====
A tutorial on how to build a Python package.

"""


# %% IMPORTS
# Future imports (only required if py2/py3 compatible)
from __future__ import absolute_import, division, print_function

# TuPy imports
from .__version__ import version as __version__
from . import fibo

# All declaration (only import these definitions with "from tupy import *")
__all__ = ['fibo']

# Author declaration (optional)
__author__ = "Ellert van der Velden (@1313e)"
