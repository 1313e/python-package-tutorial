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

# If everything from fibo must be bound to tupy in addition to tupy.fibo,
# uncomment the following line
from .fibo import *

# If everything from fibo must also be imported with "from tupy import *",
# uncomment the following line in addition to "from .fibo import *" above
__all__.extend(fibo.__all__)

# Author declaration (optional)
__author__ = "Ellert van der Velden (@1313e)"


# %% EXECUTE INITIALIZING CODE
pass
