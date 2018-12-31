Required file in a Python package
=================================
When creating a Python package, the following files are required or highly recommended:

- A directory containing the actual package.
  It is recommended to give it a simple, all lowercase name that is the same as its namespace (the name it is imported with);
- A Python-specific ``.gitignore`` file (assuming the package is in a git repo), which lists expressions and identifiers that are commonly used in Python, that should be ignored by git.
  An example of this are the ``build`` and ``dist`` directories that are created when a Python package is built (which are often Python version and OS-specific);
- A ``LICENSE`` file with the software license of this package.
  When creating a file in a GitHub repo and naming it ``LICENSE``, it will automatically provide you with a bunch of license templates to pick from;
- A ``MANIFEST.in`` file, which lists all non-Python files that should be included in the distribution of the package.
  By default, one should put the license, readme and requirements files in here.
  If the package comes with any data files, they should be listed here.
  It supports the use of wildcards ('*') and recursive includes ('recursive-include');
- A readme file, which can be written in ReStructured Text (``README.RST``) or MarkDown (``README.MD``), with RST being more versatile.
  This file should give a detailed description of the package, including what it is for, how to install it, basic ways of using it and more.
  It is also fairly common to use `badges`_ at the top of the readme file that give a status overview of the package (e.g., supported Python versions, latest released version, license, CI status).
  This file can also be used as the 'long_description' in the ``setup.py`` file, which allow it to show up on PyPI.
  Note that this is written in a readme file and therefore theoretically speaking incorrect;
- A ``requirements.txt`` file, listing all the Python package requirements of this package.
  There are many different ways of listing them, but this is by far the easiest and most common way, since it can be imported into the ``setup.py`` file.
  Every requirement should be put on a separate line, using no spaces anywhere;
- A setup configuration file called ``setup.cfg``.
  This file contains several configuration settings for specific actions, like creating a distribution, performing pytests and more.
  If your package is to be built and distributed in the same way (independent of OS or compatible Python version), use the file included here.
  This file is not necessary, but it is usually a good idea to include anyway;
- A setup file called ``setup.py``, which describes the process that needs to be executed in order to install the package.
  There are multiple different ways of making one, with the most commonly used method being the 'setup()' function from the ``setuptools`` package.
  This package is now supplied by default in every Python distribution and therefore does not need to be installed manually.
  See `its documentation<https://setuptools.readthedocs.io/en/latest/setuptools.html>`_ for a full rundown of all the arguments that can be used.
  The included ``setup.py`` file shows the default lay-out of a setup-file, but many more arguments can be given.
  Keep in mind that the lay-out would be much different if the Python package requires C-extensions or different installations depending on machine/architecture/etc;
- And finally, a place to store the version of the package.
  There are also many different ways to store this (and only storing it once).
  I personally prefer to create a ``__version__.py`` file inside the package directory (so, ``testpy/__version__.py``) and executing this file inside the ``setup.py`` file.
  This allows the version to be read without requiring the package to be installed, while it can also be read in by the ``__init__.py`` file as the ``__version__`` property.
  This then automatically hides the actual file from the user.

If all of these files are present, and the package directory itself contains an ``__init__.py`` file, the package can be installed and imported.
Try playing around a bit with the settings in the ``setup.py`` file and reinstall the package to see the changes.
The location of an installed package can be found easily by importing it and executing the following:

	>>> import testpy
	>>> testpy.__file__

This returns the path to the installed and imported ``__init__.py`` file.

See next tutorial for the basic layout of the package itself.

.. _badges: https://shields.io/#/
