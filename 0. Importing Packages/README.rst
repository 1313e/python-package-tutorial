How does importing a Python package work?
=========================================
When executing the following::

	>>> import testpy

Python will attempt to import a package that is called ``testpy``.
This is done in the following order (if more than one case applies, the first valid case is used and the remaining cases are ignored):

- If the current working directory contains an *importable* directory named ``testpy``, it is imported;
- Else, if the current working directory contains a Python file named ``testpy.py``, it is imported;
- If neither of these apply, Python will search the system PATH-variable for a package named ``testpy``.
  If the package is a directory (not a file), its name can be different from ``testpy`` as long as it is registered with the correct import name;
- If this fails as well, an ``ImportError`` is raised.

Try changing the names of the ``testpy.py`` file and/or the ``testpy`` directory to the name of an installed package to see this in action.

In order to make a directory *importable* (which is required to register it as a Python package), it must have an ``__init__.py`` file at the root of the directory.
This file must have this exact filename, but it can be empty if preferred.
Its purpose will be discussed later.
Try changing the name of the ``testpy/__init__.py`` file to see that the local directory becomes unimportable and will be ignored.

