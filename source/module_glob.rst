glob module
#################

:Status: in progress 

The :mod:`glob` module implements globbing of directory contents. 


.. seealso:: :func:`os.listdir()`, :mod:`os`

Quick start
=============

::

    >>> import glob
    >>> glob.glob('/home/user', '*')

The glob.glob returns the list of files with their full path (unlike :func:`os.listdir()`) and is more powerful
than os.listdir that does not use wildcards.

In addition, :mod:`glob` contains the :mod:`os`, :mod:`sys` and :mod:`re` modules.


wildcards
===========

========= ================================================ =========================================================
Wildcard   Matches                                          Example
========= ================================================ =========================================================
`*`        any characters                                  `*.txt`   matches all files with the txt extension
?          any one character                               `???`     matches files with 3 characters long
[]         any character listed in the  brackets           `[ABC]*`  matches files starting with A,B or C
[..]       any character in the range listed in brackets   `[A..Z]*` matches files starting with capital letters
[!]        any character listed in the  brackets           `[!ABC]*` matches files that do not start with A,B or C
========= ================================================ =========================================================


methods
=========

:meth:`glob.glob1` is equivalent to :meth:`glob.glob`. Instead of providing a pathname, you decompose it into a dirname and a pattern. So::

    glob.glob('/home/user/*')

becomes::

    glob.glob1('/home/user/', '*')



TODO

::


    glob.fnmatch           
    glob.has_magic        
    glob.iglob            
    glob.glob0             glob.magic_check
    



