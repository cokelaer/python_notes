Glossary
===========

.. glossary::

    Binary Distribution

        A :term:`Built Distribution` that contains compiled extensions.

    Built Distribution

        A :term:`Distribution <Distribution Package>` containing files and metadata, which can be moved 
        to another location on the target system, to be installed. :term:`Wheel` is such a format, 
        whereas distutil’s :term:`Source Distribution <Source Distribution>` is not, in that 
        it requires a build step before it can be installed. 

    Distribution Package

        A versioned archive file that contains Python :term:`packages <Import 
        Package>`, modules, and other resource files that are used to distribute a 
        Release. The archive file is what an end-user will download from the 
        internet (e.g., Pypi) and install.

        It may be confusing to use only **package** to refer to a distribution since
        an :term:`Import Package` is also commonly called a "package". Besides
        distribution could refere to another kind of distribution (e.g. a Linux 
        distribution or the Python language distribution).

    Egg
    
        A :term:`Built Distribution` format introduced by setuptools, which is being 
        replaced by Wheel.


    Extension Module
    
        A :term:`module <Module>` written in the low-level language of the Python 
        implementation: C/C++ for 
        Python, Java for Jython. Typically contained in a single dynamically loadable 
        pre-compiled file, e.g. a shared object (.so) file for Python extensions on Unix, 
        a DLL (given the .pyd extension) for Python extensions on Windows, or a Java 
        class file for Jython extensions.


    Known Good Set (KGS)

        A set of distributions at specified versions which are compatible with each other. 
        Typically a test suite will be run which passes all tests before a specific set of 
        packages is declared a known good set. 


    Import Package

        A Python module which can contain other modules or recursively, other packages.
        An import package is more commonly referred to with the single word "package", 


    Module
    
        The basic unit of code reusability in Python, existing in one of two types: 
        :term:`Pure Module`, or :term:`Extension Module`.


    Project

        A library, framework, script, plugin, application, or collection of data or 
        other resources, or some combination thereof that is intended to be 
        packaged into a :term:`Distribution <Distribution Package>`.

        Since most projects create Distributions using distutils or setuptools, 
        another practical way to define projects currently is something that 
        contains a setup.py at the root of the project src directory. 

        Python projects must have unique names, which are registered on PyPI. 


    Pure Module
    
        A :term:`module <Module>` written in Python and contained in a single .py file (and possibly 
        associated .pyc and/or .pyo files).


    Python Package Index (PyPI)
    
        PyPI is the default Package Index for the Python community. 
        It is open to all Python developers to consume and distribute their distributions.


    Requirement
    
        A specification for a :term:`package <Package>` to be installed using pip
        

    setup.py
    
        The project specification file for distutils and setuptools.


    Source Archive
        
        An archive containing the raw source code for a Release, prior to creation of 
        an :term:`Source Distribution` or :term:`Built Distribution`.

    
    Source Distribution
    
        A :term:`distribution <Distribution Package>` format (usually generated using 
        python setup.py sdist) that provides metadata and the essential 
        source files needed for installing by a tool like pip, or for 
        generating a :term:`Built Distribution`.


    System Package
    
        A package provided in a format native to the operating system, e.g. 
        an rpm or dpkg file.


    Virtual Environment

        An isolated Python environment that allows packages to be installed for use 
        by a particular application, rather than being installed system wide. 

    Wheel
    
        A Built Distribution format introduced by PEP427. The Wheel Binary Package 
        Format 1.0, which is intended to replace the Egg format. Wheel is 
        currently supported by pip.





:References: https://packaging.python.org/en/latest/glossary.html#term-distribution-package        
