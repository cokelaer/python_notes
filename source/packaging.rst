Packaging
##############

:Status: In progress
:Last Reviewed: 

What is a package ?
=========================

A Python package allows you to combine several modules within a common name (package).
It is a directory that contains the special file **__init__.py**. This file can be empty but must be present. Here is an example of a package called **Package1** contained in the a dicretory called **Project**::


    .
    └── Project
        ├── setup.py
        ├── Package1
            ├── module1.py
            ├── module2.py
            ├── module3.py
            ├── __init__.py


Although the **__init__** file can be empty, it may be used to add statements. It may be used to import specific functions.


What is a project ?
==========================

In the structure above, the special file **setup.py** contains the mechanism that will allow you to build a project. A project may contain several packages.


The setup file can be written in different ways.  Here is one minimalist example::

    from distutils.core import setup
    setup(name='Project',
        version='1.0',
        py_modules=['NameOfModule'],
    )

You can then install it by typing this command in a command line interface::

    python setup.py install

Or create a distributable file (stored in dist/ directory)::

    python setup.py sdist

Interest of a package/project
===============================
Project can be :

* installed with pip or easy_install.
* specified as a dependency for another project.
* downloaded for installation or to run tests.
* complemented with tests and to distribute documentation.




.. todo:: setuptools, pypi





resources: https://packaging.python.org/en/latest/
https://docs.python.org/2/distutils/setupscript.html
http://www.scotttorborg.com/python-packaging/




