
======
About 
======

The main goal of this documentation is to make available notes I'm taking about the Python language. It does not pretend to be a thourough tutorial on Python. Very good tutorials and books already exist indeed (see for instance the `official Python website <http://docs.python.org/>`_ or `dive into python <http://diveintopython.org/>`_  and take a look at the bibliography section :ref:`biblio`). 

These notes may be useful for beginners or more experienced Python developers, which is the main reason for making it public. Some sections are ready for reading (:ref:`main_beginners`, :ref:`main_advanced`) and some others maybe in development (:ref:`main_modules`).

Before starting, if you want to know why to use Python, just have a quick look in the :ref:`advantage_vs_drawback` section. 

.. note:: you can link this page to the following tiny URL: http://tinyurl.com/d2k7bqe

==========================
Before starting
==========================
Python provides a shell where you can type commands and see their immediate effect, however, we strongly recommend to install `ipython <http://www.ipython.org>`_ instead, which provides nice features such as tab completion. In order to start an interactive python shell, just call the **ipython** executable. In interactive mode, the prompt is repesented by the >>> signs. Most of the code snippets and examples provided here appear as follows::

        >>> variable = 1
        1

where python codes are preeceded by the >>> signs and outputs are shown without. For your convenience, the button in the top right corner removes the >>> signs (and the output) so as to permit a convenient copy/paste in your shell.

Just a few comments about Python syntax before starting:

    * No ; character at the end of a line, just a return carriage
    * Indentation is important and used to separate code blocks
    * everything is an object

And now for something completely different, see the next section for more information about Python syntax.

.. _main_beginners:

=========================
Essential Python syntax
=========================

The following links present some basic notions about the Python language. 
Although Python is an Object Oriented language (everything is an object in Python), you do not need it to start programming in Python. We will have a very quick overview in this section. 

.. toctree::
    :numbered:
    :maxdepth: 1

    basics.rst
    variables
    numbers.rst
    data_structures.rst
    functions.rst
    print.rst
    module.rst
    files.rst
    builtins.rst
    pythonpath.rst
    coding_conventions.rst

.. _main_advanced:

==================================================
Advanced topics on the Python language
==================================================

Here are more advanced notions that will be needed to improve
either the robustness of your code or to code performance.

.. toctree::
    :numbered:
    :maxdepth: 1

    iterators.rst
    generators.rst
    exceptions.rst
    decorators.rst
    classes.rst
    namespace.rst
    packaging.rst
    sorting.rst
    boolean.rst
    tricky.rst
    slots.rst



.. _main_modules:

========================
Useful standard Modules
========================

There are more than 300 modules available in the `Python reference guite <http://docs.python.org/2/library/index.html>`_ covering many different aspects of computer science. Some of them are covered here below.

.. toctree::
    :numbered:
    :maxdepth: 1

    modules.rst
 
.. _main_libraries:

==================
Other resources
==================

This tutorial focuses on the standard Python library and its standard modules.
Note, however, that there are lots of external libraries. If you are interested
to analyse/visualise data, this non-exhaustive list will help you to start with
your data:


=============== ================================
=============== ================================
  matplotlib    Plotting tools `a la` Matlab
  numpy         Manipulating arrays efficiently
  scipy         Lots of numerical analysis tools
  networkx      Playing with graph
  igraph        Playing with graph
=============== ================================

The website to look at before starting any project is `Pypi <https://pypi.python.org/pypi>`_, which host thousands of projects. You may found was you are trying to do there...


=========
Changelog
=========

.. toctree::

    changelog.rst
    todo.rst

.. toctree::
    :maxdepth: 2

    biblio.rst

.. toctree::
    :hidden:
    :maxdepth: 2

    why_python.rst
    biblio.rst


.. toctree::

    module_anydbm
    module_readline
    misc
