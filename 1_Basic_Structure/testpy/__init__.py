# -*- coding: utf-8 -*-

"""
TestPy
======
A tutorial on how to build a Python package.

"""


# %% IMPORTS
# Future imports (only required if py2/py3 compatible)
from __future__ import absolute_import, division, print_function

# TestPy imports
from .__version__ import version as __version__
from . import fibo

# All declaration (only import these definitions with "from testpy import *")
__all__ = ['fibo']

# If everything from fibo must be bound to testpy in addition to testpy.fibo,
# add the following lines
#from .fibo import *
#__all__.extend(fibo)

# Author declaration (optional)
__author__ = "Ellert van der Velden (@1313e)"
