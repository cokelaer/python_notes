Coding Conventions
======================

:reference: PEP8 Style Guide for Python code

coding conventions are not required strictly speaking. The code will still work.
However, most of python developers follow those rules so it is better to use
them.

general
---------

* Indentation: use 4 spaces for one indentation level
* Never lix up spaces and tabs
* maximum line length:  79 characters. If too long, you can either place the
  statement inside parentheses/brackets/braces or use the backslash characters,
  which looks better
* Blank lines are used to separate block of code. 2 Blank lines are used to separate function and classes. Methods within a class are separated with one blank line.
* Encoding: use latin-1 or utf-8, which is the preferred over latin-1 in python
  3.0  . all identifiers should use ascii only

imports
------------ 

* imports should be on different lines. Nevertheless it is accepted on one line
  if using the **from** keyword::

      import os
      import sys
      from subprocess import PIPE, Popen

* imports are put at the top of the file after module comments and docstrings.
* imports are groupd in this order:

  #. standard library
  #. related third party imports
  #. local modules

* relative imports are discouraged

whitespaces
---------------

* add one space after commas::

    x, y  # YES
    x,y   # NO

* avoid extra whitespaces inside parenthese::

    func1(x[1], {'y':2})    # YES
    func1( x[1], {'y':2} )  # NO

* avoid whitespaces before parentheses (function, classes) or
  brackets(dictionary, slicing)::


    func1(x)    # YES 
    func1 (x)   # NO

    x[1]        # YES
    x [1]        # NO

* more than one space around the assignment operator (or others)::

    x = 1   #YES

::     
    x   = 1
    xyz = 1  #NO


* Use one spaces on each side of the operators::


  1 == x
  x += 1
  x ** 2
  c = (a + b) * (c + d)

* do not use spaces around = character when it indicates a keyword argument.


* avoid compound statements (multiple) one a single line. Write this code::

    if x == 1:
        print(x)

instead of::

    if x == 1: print(x)

comments
---------

* keep comments up-to-date !!
* should be sentences. do not capitalise identifiers.
* block comments: same level of indentation as the code.
* use inline comments sparingly:: 

    x = x + 1 # Increment 1

docstrings
--------------

* docstrings should be provided for classes and functions, methods, modules. Not
  required for private methods but a comment should be provided.


subversion
-----------

These lines could be included after the module's docstring::


    __version__ = "$Revision: $"
    # $Source$

naming conventions
---------------------




* names to avoid: character `l` (lowercase el), `O` (uppercase oh) and `I`
  (uppercase eye) as single character variable. I some devices/fonts they can be confused with number
  1 and 0. 


* class names and exceptions: use CapWords
* function and method names and instance variable: lowercase with underscores to
  separate names.
* function and method names: use **self** for instance method and **cls** for class
  method.  

* if a variable clashes with existing keyword, it is better to append an
  underscore rather than altering the name.

classes
---------

* public attribute should have no leading underscores
* classes private/public attributes: by defautl make you attribute private.
  easier to change to public than the inverse.

others
--------
* Comparison to None should always be done with *is** and **is not**.
* Be careful with **if x**. Use **if x is not None** instead since x may be
  changed to a value that can either True or False.
* use base-class exceptions.  
* Use raise ValueError(message) instead or raise ValueError, message
* type comparison should use **isinstance** instead of direct comparison or
  **type**.

