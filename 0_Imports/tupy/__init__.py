# -*- coding: utf-8 -*-

"""
TuPy
====
A tutorial on how to build a Python package.

"""


# %% IMPORTS
# Future imports (only required if py2/py3 compatible)
from __future__ import absolute_import, division, print_function

# Package imports
import numpy as np

# All declaration (only import these definitions with "from tupy import *")
__all__ = ['fib_arr', 'fib_val']


# %% FUNCTION DEFINITIONS
# This function calculates the value of the Fibonacci sequence at given index
def fib_val(index):
    """
    Returns the value of the Fibonacci sequence at given `index`.

    Parameters
    ----------
    index : int
        Index of requested Fibonacci number.

    Returns
    -------
    value : int
        Fibonacci value at given `index`.

    """

    # Check if index is non-negative
    if(index < 0):
        raise ValueError("Input argument 'index' must be 0 or higher!")

    # Initialize i=0 and i=1
    a = 0
    b = 1

    # If index is not 0 or 1, keep calculating the next two numbers
    for _ in range(1, index, 2):
        # Save the even index as a and the odd index as b
        a = a + b
        b = a + b

    # If index is even, return a
    if not index % 2:
        return(a)
    # Else, return b
    else:
        return(b)


# This function calculates the Fibonacci numbers up to given index
def fib_arr(index, inclusive=False):
    """
    Returns the values of the Fibonacci sequence up to given `index`.

    Parameters
    ----------
    index : int
        Index of requested Fibonacci number.

    Optional
    --------
    inclusive : bool. Default: False
        Whether or not to include the Fibonacci number at given `index`.

    Returns
    -------
    array : :obj:`~numpy.ndarray` object of 64-bit ints
        Array of Fibonacci numbers up to given `index`.

    """

    # Check if index is non-negative
    if(index < 0):
        raise ValueError("Input argument 'index' must be 0 or higher!")

    # Raise index by 1 if inclusive is True
    if inclusive:
        index += 1

    # Initialize Fibonacci array
    array = np.zeros(index, dtype=np.int64)

    # If index is at least 2, add 1 as well
    if(index > 1):
        array[1] = 1

    # Loop over all remaining indices and calculate their values
    for i in range(2, index):
        array[i] = array[i-2] + array[i-1]

    # Return array
    return(array)


# %% EXECUTION
# The code below is only executed if the file itself is executed with
# "$ python __init__.py" or "exec(open('__init__.py', 'r').read())".
# It is ignored if the file is imported by an other script.
if(__name__ == '__main__'):
    print("The Fibonacci number at index 6 is %i." % (fib_val(6)))
    print("The Fibonacci numbers up to index 9 are %s." % (fib_arr(9)))
