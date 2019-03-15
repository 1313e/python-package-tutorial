Basic structure of a Python package
===================================
A Python package is usually made up of four different components:

- Dunder files: Python files that have two leading and two trailing underscores.
  The most commonly used dunder file is the ``__init__.py`` file, which makes the current directory *importable* and flags it as a Python subpackage;
- Submodules: Python files that are not dunder files.
  Submodules are importable from their respective subpackage, and usually provide definitions of classes and functions;
- Subpackages: Importable directories, including the main namespace.
  Subpackages are also importable from their respective subpackage, and usually provide access to submodules and other subpackages.
  Commonly, subpackages automatically import definitions of their submodules (like the ``__init__.py`` file importing the definitions of the ``fibo`` submodule);
- Package data: All files in the main namespace that are not dunder files or submodules.
  These are commonly data or configuration files that are required by the package when performing specific operations.
  If they are not located inside an importable directory, the `include_package_data` keyword in the ``setup.py`` file must be set to ``True``.

I will discuss these different components in more detail below.

Dunder files
------------
In Python, anything that has two leading and two trailing underscores, is called a *dunder* (Double UNDERscore) directory/file/method/function/attribute/property/etc.
They are also sometimes referred to as *magic* ..., as they often hold a special meaning and are called by Python itself.
Because of this, it is widely regarded a bad idea to introduce your own dunder names (except for files), as this may cause code to break in weird ways when Python adds the same dunder name for a specific internal operation.
Understanding how dunder files (and other dunder objects in general) work and are used by Python, can be quite useful in many different scenarios when making a package.
I will explain other dunder objects later on.

The most commonly used dunder file is by far the ``__init__.py`` file, which I briefly described in ``0_Imports``.
This dunder file makes a directory importable as a Python (sub)package, regardless of its contents.
Not including an ``__init__.py`` file will not necessarily mean that a directory cannot be imported (as explained in ``0_Imports``).
However, many automated routines will fail to recognize the directory as part of a package and all of its contents would have to be imported explicitly by the user to become accessible.
As this dunder file is core to all subpackages, I will explain its uses more in `Subpackages`_.

Other dunder files are much less common and it is likely that one never needs them besides ``__version__.py`` (unlike dunder methods or attributes, of which there are many useful ones).
Some examples of other dunder files include:

- ``__config__.py``: Python script that contains used configuration settings during package build;
- ``__version__.py``: Contains package versioning information;
- ``__main__.py``: Python script for when a subpackage is executed (similar to the ``__main__`` attribute of a submodule);

When using a package, one may notice that a dunder directory called ``__pycache__`` has been created.
This directory holds the compiled versions of all the submodules in the corresponding subpackage, which allows for the package to be imported faster (as it does not need to be compiled again).
Before Python 3, this directory did not exist, but instead the compiled Python files were located within the subpackage itself.
This was deemed messy (for obvious reasons) as well as dangerous, as these files were not unique to any Python version or implementation (e.g., CPython, PyPy, Jython, RPython, etc.).
Starting with Python 3, the compiled Python files were moved to the ``__pycache__`` directory as well as being made version/implementation dependent.

If a subpackage is imported, Python will still check whether or not any changes have been made to any submodule since it was last compiled, and will recompile the submodule if this is the case.
Therefore, emptying the ``__pycache__`` directory is not necessary in many cases, except when the path of a submodule changes and sometimes when using a different OS.


Submodules
----------
Submodules are the heart and soul (basically) of any Python package.
It is usually a Python file (but can also be a C or Fortan file if these languages are used as extensions), which contains the definitions of mostly classes and functions.
Whenever a submodule is imported (implicitly or explicitly), all code in the entire submodule is executed except for anything inside an ``if __name__ == '__main__'`` statement.
Any namespaces created during this process, like variables, classes and functions but also other imported submodules and subpackages, will be bound to the namespace of the imported submodule.
The namespace of subpackages/submodules is given by its ``__name__`` property, where the name of a Python process is always ``'__main__'``.
One can use the ``dir()``-function to access a list of everything bound to a given namespace (or, since Python 3, by checking its ``__dir__`` property).

**Note:** As described before in ``0_Imports``, namespaces are only imported if they do not already exist in the current context.
However, namespaces are only created if they were imported successfully.
Therefore, importing a submodule A, which imports a submodule B, which imports submodule A, would create an infinite recursive loop of imports.
However, Python is smart enough to detect that such an infinite loop is going to be created, and simply raises a ``NameError``, telling you that submodule A does not exist (in the current context).
For this reason, it is advised to make sure that submodules (or subpackages) only import namespaces that do not require the to-be imported namespace.
If this is unavoidable for some definitions, one can perform such imports inside the function/class definition itself (which will simply grab the namespace and make it locally available).

Submodules (and subpackages) have quite a few important dunder attributes, of which some are useful to be modified by the user.
I give an overview of the most important ones below:

- ``__all__``: A list of strings with the names of all (accessible) objects that need to be imported if ``from ... import *`` is used.
  If not set by the user, ``from ... import *`` will automatically import all namespaces (including other imported packages) that do not start with an underscore;
- ``__author__``: Name of the author of this submodule/subpackage, commonly only set for the top level package.
  It does not exist if not set by the user;
- ``__dict__``: Python dictionary containing ALL objects accessible in this namespace.
  This includes all builtin objects, global attributes and environment variables;
- ``__dir__``: Function that returns a list of all namespaces bound to this submodule/subpackage.
  Note that in Python 2, not all submodules/subpackages (or any object) necessarily have this attribute;
- ``__doc__``: The docstring that this submodule/subpackage has;
- ``__file__``: The path to this submodule/subpackage;
- ``__name__``: The namespace of this submodule/subpackage;
- ``__package__``: The subpackage this submodule belongs to.
  It is the same as ``__name__`` for subpackages;
- ``__version__``: Version of this subpackage/submodule, commonly only set for the top level package.
  It does not exist if not set by the user.

In some cases a package can have a submodule that only provides a single definition, like the definition of a large Python class.
In this case, it is probably not desirable to have the submodule namespace available.
By giving the submodule a name that has a single leading underscore and importing the definition in the ``__init__.py`` file, you can hide the submodule from the user.
For example, renaming ``fibo.py`` to ``_fibo.py`` would hide the submodule, but since all of its definitions are already imported, they are still available.

Subpackages
-----------
Subpackages are basically the same thing as the package directory itself (e.g., ``tupy`` in this case), except that they are not at the top level, but rather part of a bigger package.
They are mainly used to give structure to a Python package, avoiding having to put every single submodule in the top level directory.
Using subpackages and submodules accordingly and properly, can really improve the user experience of your package.
Having too many subpackages often leads to tedious searching, while not having enough subpackages overloads the user with definitions it does not want or expect.
It is therefore usually a good idea to think about what you want your user to see when they import your package.

A package that I often look at for structure ideas, is the `NumPy`_ package.
In NumPy, one can see that for example many base definitions are located in the ``core`` subpackage (``numpy/core``).
They are however still imported to be accessible at the top level (I will discuss this in a bit), but it makes the overall structure much more readable and clean.

.. _NumPy: https://github.com/numpy/numpy


A subpackage is, like the top level package itself, a directory that contains an ``__init__.py`` file, making it importable.
Its functionality is quite similar to a submodule, except that it usually contains submodules and subpackages rather than functions and classes (although the latter is perfectly possible to do).
Because executing a directory is not possible, importing a subpackage will cause the included ``__init__.py`` file to be executed instead.
The execution of the ``__init__.py`` proceeds in the exact same way as when a submodule is imported/executed.

When making a subpackage, it is pretty common to import all definitions from all submodules that it has (but not other subpackages), in addition to the submodules themselves (such that they can be added to ``__all__``).
This allows the user to access these definitions one level higher than where they are actually located.
A simple example of this is given in the ``tupy/__init__.py`` file, with lines 24 and 28.
This will cause everything from the ``fibo`` submodule to be imported and added to the ``__all__`` variable of ``tupy``.
This makes them available at the ``tupy`` level in addition to the ``tupy.fibo`` level (where the definitions are located).

Doing this also has an other advantage, namely that only those definitions declared in ``__all__`` will be accessible at the subpackage level.
This is useful when a submodule contains many different definitions and imported namespaces, which should not be visible to the user.
One can see an example of this with the ``fibo`` submodule by executing the following:

    >>> import tupy
    >>> dir(tupy)
    >>> dir(tupy.fibo)

One will notice that, besides the dunder attributes and the future imports, ``tupy.fibo`` also has ``np`` bound to itself (which is caused by the ``import numpy as np`` statement), which ``tupy`` does not have (although it obviously has the ``fibo`` submodule).
Of course, in this example, it is only a single external namespace/definition that was imported in the submodule, but in big packages, it can easily reach tens to hundreds.
As before, one can see this effect very clearly in a big package like NumPy:

    >>> import numpy as np
    >>> len(dir(np.linalg))
    >>> len(dir(np.linalg.linalg))

The second statement reports a much lower number than the third, as the ``np.linalg`` subpackage imports all definitions from the ``np.linalg.linalg`` submodule, but does not import anything that was not defined in that submodule.
This is also where the usefulness of the ``__all__`` variable comes in, and I would recommend to always define the ``__all__`` variable in every submodule and subpackage.
An additional benefit of using the ``__all__`` variable, is that one will never have to update the ``__init__.py`` file of a subpackage when a submodule has received a new definition.
Simply adding the name of that definition to the ``__all__`` variable in the submodule will automatically cause its parent subpackage to import it as well.
Of course, it is also possible to import everything from a subpackage into a subpackage (basically skipping two levels instead of one), but this is only recommended in very specific cases.


Package data
------------
Package data involves basically every file that is not a dunder file or submodule.
This includes for example the ``README.rst``, ``requirements.txt`` and ``LICENSE`` files, but also any data or configuration files that are inside the package.
Unless there is a good reason not to, it is often a good idea to set the `include_package_data` keyword in the ``setup.py`` file to ``True``.
This will guarantee that any file that is found inside the top level directory and is also specified by the ``MANIFEST.in`` file, will be included in the package distribution.


In the next tutorial, I will discuss how to structure and document code in a readable way.
