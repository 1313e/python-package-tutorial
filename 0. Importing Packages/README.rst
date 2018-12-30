How does importing a Python package work?
=========================================
When executing the following::

	>>> import testpy

Python will attempt to import a package that is called ``testpy``.
This is done in the following order:
- If the current working directory contains an _importable_ directory named ``testpy``, it is imported;
- Else, if the current working directory contains a Python file named ``testpy.py``, it is imported;
- If neither of these apply, Python will search the system PATH-variable for a package named ``testpy``.
  If the package is a directory (not a file), its name can be different from ``testpy`` as long as it is registered with the correct import name;
- If this fails as well, an `ImportError` is raised.
