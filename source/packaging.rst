Packaging
##############

:Status: In progress
:Last Reviewed: 


Interest of a packaging
===============================

Project can be :

* installed with **pip** or easy_install.
* specified as a dependency for another project.
* downloaded for installation or to run tests.
* complemented with tests and to distribute documentation.

What is a package (Import Package) ?
=====================================

Packaging in Python could be a bit tricky. The terminology itself could be also confusing.
so, let us start with some terminology and define what is a package, a project

What is commonly called a **package** could be in fact a :term:`distribution package <Distribution Package>` or an :term:`import package <Import Package>`. 


A Python package (Import Package) allows you to combine several modules to be imported from the Python
shell (or script) under a given name. In practice, it is a directory that contains one or more python files (.py extension) **and** a special file named **__init__.py**. This file can be empty but must be present. Here is an example of an import package called **Package1**, which is contained in the a dicretory called **Project**::


    .
    └── Project
        ├── setup.py
        ├── project
            ├── module1.py
            ├── module2.py
            ├── module3.py
            ├── __init__.py
        


Although the **__init__** file can be empty, it may be used to add statements (e.g., version or pre-processing). It may be used to import specific functions from the package so that the user knowns what are the important functionalities.


What is a project ?
==========================

In the structure above, the special file **setup.py** contains the mechanism that will allow you to build a project and to distribution a :term:`Distribution Package`. A project may contain several import packages as shown in the tree structure above.


Project with a single package
================================

The setup file can be written in many different ways depending also on the tree structure.  
Here is one minimalist example based on the previous example::

    from setuptools import setup
    setup(name='project',
        version='1.0',
        packages=['project'],
    )

You can then install it by typing this command in a command line interface::

    python setup.py install

Or create a distributable file (stored in dist/ directory)::

    python setup.py sdist

Then, open a shell and you should be able to import one of the package from the project::

    import project
    from project import module1
    module1.func()

.. note:: package names are in lower case (convention)
.. note:: project name is also in lower case (convention). However, the name of the main directory itself could be different: it is irrelevant here.


Tuning what is imported
============================
By default with an empty __init__ file, the completion will show (after import project) only the module names. You may want to add aliases to functions or classes that are commonly used. In the __init__ of a package, you can add imports such as::


    from .module1 import func


Then, these aliases will be automatically available from the project itself::

    import project
    project.func() # accessible directly !



Setuptools
==================

The **setup.py** python script has many options. We've seen the **install** and **sdist** cases. 
The other useful option is **develop**, which can also install the package with a symlink, so that changes to the source files will be immediately available. This is very handy for development.

However, be aware not to mix install and develop modes.

Where are packages/files installed ?
==========================================

Depends on your system but for instance for a Python2.7 under linux, it should be in 
/usr/lib/python2.7/site-packages . If you have a virtual environment, it will be in the virtualenv directory under /lib/python2.7/site-packages


Sharing your package
=====================

::

    python setup.py sdist

will create a tar gzipped file in ./dist/project-1.0.tar.gz    


pypi
========

::

    python setup.py register
    python setup.py sdist upload

Your distribution package (project) should now be on pypi and you can check it by typing::

    pip install <project name>


Now, this would work only if you have provided some minimal metadata, which were not provided in the previous example. This include information such as the author name.


Metadata 1
================

::

    from setuptools import setup
    setup(name='project',
        version='1.0',
        packages=['project'],
        description='description of the project',
        url='http://github.com/',
        author='whoever',
        author_email='whoever@example.com',
        license='MIT',
        install_requires=['pylab'],
        ],
    )


Metadata 2
================

There are other parameters commonly used in the setup function. First, you may want a longer 
description stored in a README file. First, add a README.rst (or .md), which can be read within
the setup.py file (note also that we have added keywords):: 

    from setuptools import setup

    with open("README.rst", "r") as fh:
        readme = fh.read()

    setup(name='project',
        version='1.0',
        packages=['project'],
        description='description of the project',
        long_description=readme,
        keywords='example setuptools'
        url='http://github.com/',
        author='whoever',
        author_email='whoever@example.com',
        license='MIT',
        install_requires=['pylab'],
        ],
    )

If you add non-python files such as the README.rst, you should include them in a special file
called **MANIFEST.in** if you want setuptools to distribute it in the source distribution::


    include README.rst
    include doc/*.rst


If you want those files to be copied in the site-packages, you will need to supply ::


    include_package_data=True 

as an extra parameter in the setup function.

classifiers
==============


::

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
    ],

.gitignore
====================
In the project, you can also add a .gitignore file if you use git.

::

    # Compiled python modules.
    *.pyc

    # Setuptools distribution folder.
    /dist/

    # Python egg metadata, regenerated from source files by setuptools.
    /*.egg-info
    /*.egg


setup.cfg
============

A special file that could be provided to overrite contents of the setup.py file.



More packages
=================


::


    from setuptools import setup, find_packages
    setup(name='project',
          version='1.0',
          packages=find_packages(),
     )

::

    ├── project
    │   ├── dna.py
    │   ├── extra
    │   │   ├── __init__.py
    │   ├── __init__.py


    import project
    project.extra ## access to a sub package
    project.dna   ## access to a module








resources: 
-------------

* https://packaging.python.org/en/latest/
* https://docs.python.org/2/distutils/setupscript.html
* http://www.scotttorborg.com/python-packaging/




