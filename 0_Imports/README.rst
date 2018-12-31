How does importing in Python works?
===================================

Importing Python modules/packages
---------------------------------
When executing the following

	>>> import tupy

Python will attempt to import a module/package that is called ``tupy``.
This is done in the following order (if more than one case applies, the first valid case is used and the remaining cases are ignored):

- If the current working directory contains an *importable* directory named ``tupy``, it is imported;
- Else, if the current working directory contains a Python file named ``tupy.py``, it is imported;
- If neither of these apply, Python will search the system PATH-variable for a module/package named ``tupy``.
  If it is a package (directory, not file), its name can be different from ``tupy`` as long as it is registered with the correct namespace;
- If this fails as well, an ``ImportError`` is raised.

Try changing the names of the ``tupy.py`` file and/or the ``tupy`` directory to the name of an installed package to see this in action.
One can check the path to the imported package with ``>>> tupy.__file__``.

When importing a Python file (either a local or registered file), all code inside this file is executed except for code inside an ``if(__name__ == '__main__)'`` statement.
All definitions in the file will be bound to the namespace of the file itself (e.g., ``tupy.fib_arr`` and ``tupy.fib_val``).
However, when importing a directory, it can obviously not be executed.
Therefore, in order to make a directory *importable*, it must have an ``__init__.py`` file at the root of the directory.
This file is executed in the same way as the local ``tupy.py`` file, binding the definitions to the namespace of the directory.
Its uses will be discussed later.

In this directory, both the local file and local directory are set-up to work exactly the same (where ``tupy/__init__.py`` is the same as ``tupy.py``.
Try changing the name of the ``tupy/__init__.py`` file to see that the local directory becomes unimportable and will be ignored.


Importing from Python modules/packages
--------------------------------------
It is also possible to import something from a Python module/package with::

	>>> from tupy import fib_arr

Here, Python attempts to import an object (anything that can be represented in Python) called ``fib_arr`` from a Python module/package called ``tupy``.
Determining where ``fib_arr`` is imported from is done in the same way as before, but the namespace itself is not explicitly imported.
If a valid target has been found, then checking for ``fib_arr`` is done in the following order:

- If the ``tupy`` namespace contains an object called ``fib_arr``, it is imported;
- Else, if the ``tupy`` namespace is a Python package (not module) and contains a submodule/subpackage called ``fib_arr``, it is imported;
- If both of these fail, an ``ImportError`` is raised.

Keep in mind here that although the ``tupy`` namespace itself was imported, it was not explicitly imported and therefore is not accessible.
Importing ``tupy`` itself will make it accessible. 
One can see this by importing ``fib_arr`` and then checking ``>>> fib_arr``.
Even though we only imported ``fib_arr``, it still (correctly) points to ``tupy.fib_arr``.
Another way of seeing this would be by importing something from a package that modifies other packages or takes a noticeable time to import (like PRISM).
Importing the package itself afterward will not have this effect, showing it was already imported.

The difference between importing something from a package or accessing it from an imported package, is that the latter only allows access to the namespace.
What this means is that if an imported package does not import a submodule/subpackage in its ``__init__.py`` file, it will not be bound to the namespace and is thus not accessible.
Importing this submodule/subpackage using this method will make it accessible.

The ``tupy`` package has a file called ``fibo.py`` (same file as the ``__init__.py`` file), which is not imported automatically.
It can be imported however with:

	>>> from tupy import fibo

This will bind it to the ``tupy`` namespace as well, even though it has not been imported explicitly.
One can check this by comparing the outputs of the following two snippets:

	>>> import tupy
	>>> dir(tupy)

and

	>>> from tupy import fibo
	>>> import tupy
	>>> dir(tupy)

The latter snippet will show that the ``fibo`` submodule is available, while the first does not (``dir()`` shows a list of everything bound to the provided namespace).
Note that the ``fibo`` submodule can also be bound to the ``tupy`` namespace with:

	>>> import tupy
	>>> import tupy.fibo

A few uses of this will be discussed later.

See next tutorial for the basic structure of a Python package.
