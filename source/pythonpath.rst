
.. _pythonpath:

PYTHONPATH variable
###########################

module search path and pythonpath
=================================

While trying to import a module, you may have encountered the following error::

   >>>import mymodule
   Traceback (most recent call last):
       File “<pyshell#2>”, line 1, in ?
           import mymodule
   ImportError: No module named mymodule


This happens because while importing a module, the Python interpreter searches for it in certain predefined locations. These predefined locations are a set of directories that constitute the Python search path, which is defined by the current directory and the Python search path that is specified in the environment variable PYTHONPATH.

