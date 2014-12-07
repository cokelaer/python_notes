built-in functions
######################

Python contains built-in functions amongst which the standard Errors and Warnings. 

.. seealso:: See the section :ref:`exceptions` for more information about these errors.

To obtain the entire list of built-in function, type::

    dir(__builtins__)

If we ignore all the exceptions error and warnings, we have the following list:

::

    >>> [x for x in dir(__builtins__) if 'Error' not in x and 'Warning' not in x and 'Exception' not in x]
    ['Ellipsis', 'False', 'KeyboardInterrupt', 
     'None', 'NotImplemented', 'StopIteration',
     'SystemExit', 'True', '__debug__', '__doc__', '__import__',
    '__name__', 'abs', 'apply', 'basestring', 'bool', 'buffer', 'callable', 'chr',
    'classmethod', 'cmp', 'coerce', 'compile', 'complex', 'copyright', 'credits',
    'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'execfile', 'exit',
    'file', 'filter', 'float', 'getattr', 'globals', 'hasattr', 'hash', 'help',
    'hex', 'id', 'input', 'int', 'intern', 'isinstance', 'issubclass', 'iter',
    'len', 'license', 'list', 'locals', 'long', 'map', 'max', 'min', 'object',
    'oct', 'open', 'ord', 'pow', 'property', 'quit', 'range', 'raw_input',
    'reduce', 'reload', 'repr', 'round', 'setattr', 'slice', 'staticmethod',
    'str', 'sum', 'super', 'tuple', 'type', 'unichr', 'unicode', 'vars',
    'xrange', 'zip']

Brief overview 
=================

Most of the following functionalities are really standard and used throughout this documentation so they do not need to be describe. In some other cases, other section described them in depth. Here is a brief summary. 

.. index:: list, tuple, dict, set, frozenset, str, complex


Data structures, types and boolean type
-------------------------------------------
Python provides standard data structures (see :ref:`data_structures`) such as dictionary with :func:`dict`, lists with :func:`list`, immutable lists known as tuple with :func:`tuple`, string with :func:`str`, sets with :func:`set` and frozen sets with :func:`frozenset` (immutable version of set). 


Note that the :func:`str`: coerces data into a string and that it works on everything ! The behaviour can be overloaded in classes using __str__ method (see :ref:`classes`).

If you already know what __doc__ is, consider this example:

.. doctest::

    >>> # This function has no docstring, which is empty by default
    >>> def foo(data): return data*2
    >>> # the docstring is empty.
    >>> foo.__doc__
    >>> # However, coercing with str function returns the string 'None'
    >>> # so that any __doc__ can be considered as a string.


In addition, standard types are available (:func:`basestring`,  :func:`int` :func:`long` :func:`float` :func:`complex` type). The boolean type provides the `False`, `True` and :func:`bool` returns True when its argument is true. Finally, there is a special type called `None` which is False by default.

In order to know the type of an instance, you can use the :func:`type` function::

    >>> type([1, 2])
    list


Note about assertion
----------------------
* :func:`__debug__` contains a private boolean (cannot be set) that defines the assertion behaviour. Indeed, if optimisation is on (python -O), then asserts do not raise any error. This is a good reason to avoid using assertion but exception !


Conversion
------------

There are a few functions to convert a variable in hexadecimal (:func:`hex`), octal (:func:`oct`) , ordinal (:func:`ord`), string (:func:`chr`) or unicode string (:func:`unichr`)


Simpe Maths functions
---------------------
Simple mathematical functions are available: :func:`max`, :func:`min`, :func:`sum`, :func:`pow`, :func:`abs`, :func:`round`, :func:`cmp`, :func:`divmod`. 

The :func:`cmp` function compares two objects and returns 0 if the two objects are equal, 1 if the first object is greater than the second, -1 if the first object is less than the second object:

.. doctest::

    >>> cmp(1, 10)
    -1


Sequence objects (list, tuple) can also be compared. The comparison is made using lexicographical ordering: the first 2 element are compare. If equal, the 2 next elements are compared:

.. doctest::

    >>> cmp((1,2,3),(1,4,3))
    -1

If the first elements in a sequence are equal to those in a second sequence, the smaller sequence is considered to be less:

.. doctest::

    >>> cmp([1,2,3],[1,2])
    1

.. index:: callable, getattr, setattr, delattr, object, isinstance, issubclass, classmethod, staticmethod, super, id, iter, property

Object oriented language
-------------------------

There are a number of builtin functions that are related to classes. 


The function :func:`callable` returns `True` if the object can be called, `False` otherwise. Classes that have the __call__ method defined are callable. See also :ref:`classes` section.



You can manipulate attributes using :func:`hasattr`, :func:`getattr` :func:`setattr` and :func:`delattr` functions. ::

    import math
    hasattr(math, 'pi')

    getattr(math, 'pi') # equivalent to math.pi

    setattr(math, 'pi', 3.14)
    getattr(math, 'pi')

    delattr(math, 'pi')
    hasattr(math, 'pi')


The :func:`getattr` function returns any attribute of any object:

.. doctest::

    >>> getattr({}, "clear")
    <function clear>


The :func:`object` class is the most base type that should be inherited by all classes::

    >>> class Simplest(object):
    ...    pass

You can check that a variable is an instance of a class with :func:`isinstance`::

    >>> s = Simplest()
    >>> isinstance(s, Simplest)
    True

of that a class inherits from another one with :func:`issubclass`::

    >>> issubclass(Simplest, object)
    True

The :func:`format` applied on an object returns a string representation of the
object using the __format__ method if defined. Another function related to
reprensenting an object is the :func:`repr`.

The function :func:`hash` returns the hash value of an object that is an integer
value provided by the ** __hash__** method of the object. Consider using :mod:`hashlib` module
if you want to play around with hash..

.. todo::  classmethod staticmethod super id, iter, property

.. index:: input, raw_input, eval

IO related
-------------

The :ref:`files` section shows how to manipulate files with the :func:`file` type and and :func:`open` functions. 

To retrieve a line of text from standard input you can use the :func:`input` and :func:`raw_input` built-in functions.::

    number = raw_input("Enter a number")

**input** is equivalent to **eval(raw_input())**. You should use the second form because **input** expects a valid Python expression.

.. warning:: The :func:`raw_input` function has been replaced by :func:`input` in Python 3. Be aware that there is also a :func:`input` function in Python 2. In Python 3, the former :func:`input` function does not exist anymore. You would simply use eval(input('your prompt')) 


functional programming
-----------------------

See the :ref:`functional` section for an explanation of what are the :func:`map`, :func:`apply`, :func:`filter` and :func:`reduce` and :func:`zip` functions. On top of which, you can add the lambda function, which is not part of the builtin functions.





.. _builtins_iterator:

Iterators
-----------------

Iterators are objects that can be traversed through all the elements of a collection. When you loop over a dictionary or a string or a list you use the iterator of the structure itself. For instance, if you loop over a dictionary you actaully traverse its keys::

    >>> data = {"a":1,"b":2,"c":3}
    >>> for key in data:
    ...    print key
    a
    b
    c

Iterators have different behaviour depending on the object type. For instance, if you loop over a string, you get characters.

You can transform an object into an iterator using  the :func:`iter` builtin function

    >>> x = [1,2,3]
    >>> ix = iter(x)
    >>> ix.next()
    1
    >>> ix.next()
    2
    >>> ix.next()
    3
    >>> ix.next()
    StopIteration:

First, note that instead of the next method, you could use the :func:`next`
built-in function. 

When there is no more element to fetch, the :func:`StopIteration` error is raised.

**iter** can take a callable argument. For instance::

    def seek_next_line(f):
        for c in iter(lambda: f.read(1),'\n'):
            pass

The iter(callable, sentinel) can be used in such a way that the callable is called until it returns the sentinel.

.. seealso:: :ref:`iterators` section

Module related
----------------

The reload and dreload functions are used to reload a module that was imported
but has changed. This is mostly useful for developers.  See :ref:`reload`
(in the :ref:`modules`) for details.

others
----------


See :ref:`namespace_scope` for more information about :func:`locals`, :func:`globals` and :func:`vars` and :func:`dir`. 

The :func:`exit` and :func:`quit` are equivalent. You also have autocall :func:`exit` and :func:`quit` (no need for brackets). You can also use sys.exit() to specify informative error message.


The :func:`help` prints the docstring of any object.

The :func:`inter` function allows to speed up code according to the PYthon
documentation. I've personally never seen it being used but could be useful
maybe. The way it works is to add the name of key used in a dictionary into
a lookup table. The key comparison will then be done on the string pointer
rather than the string itself.

The :func:`memoryview` and :func:`buffer` functions are rarely used but
could be interesting for speeding up your code. See :ref:`buffering` section for
details.

.. todo:: coerce,  __import__ copyright, credits SystemExit Ellipsis KeyboardInterrupt Notimplemented  __debug__,  __name__, license and ::




The :func:`range` and :func:`xrange` functions generates list of integers in the specified range. :func:`xrange` is the generator version of :func:`range`. See  :ref:`introduction` for examples.

Sequence related
---------------------

The :func:`slice`, :func:`reversed` and :func:`sorted` functions can be used as
follows::


    >>> x = [4,9,1]
    >>> list(reversed(x))
    [1, 9, 4]
    >>> sorted(x)
    [1, 4, 9]

    >>> x[0:2]
    [4, 9]


More about slicing in :ref:`slicing`


Accessing the index in Python for loops
------------------------------------------


A very convenient and used function is the :func:`enumerate`. Let us give an
example::

    >>> data = [4, 9, 1]
    >>> for i, x in enumerate(data):
    ...    print(i,x)
    1, 4
    2, 9
    3, 1


You could also use another solution based on range and length of the array::

    >>> for i in range(0,len(data)):
    ...     print(i, data[i])

but this is less pythonic that using the enumerate function (i.e., it
does not use additional state variable for the counter). From a point of few of
speed, it seems to be the same though.


character encoding related
===============================

.. todo::  'unichr': <function unichr>,
.. todo::  'unicode': unicode,

Running code programmatically
================================

.. todo:: to be checked and updated.

Python provides several built-in tools to precompile and execute frequently used pieces of code.

To compile a string (could be a module, statement) into a code object use the :func:`compile` function::

    compile(string, filename, mode)

so that it can be executed by the exec statement or eval().

The filename must be a valid string, in which case mode should be 'exec'.

The mode must be 'exec' to compile a module, 'single' to compile a
single (interactive) statement, or 'eval' to compile an expression.

The flags argument, if present, controls which future statements influence
the compilation of the code.

For instance::

    eval_code = compile("a=1", "<string>", 'eval')
    eval(eval_code)


    single_code = compile("print 1", "<string>", 'single')
    eval(single_code)


    exec_code = compile(""" """)
    exec exec_code


    >>> eval("int(3.14159)")
    3



to evaluate a string or code object: eval
to evaluate a string, file object or code object: exec

to execute a source-code file, use :func:`execfile`::

    >>> f = open("mymod.py", "w")
    >>> f.write("print('hello')")
    >>> f.close()
    >>> execfile("mymod.py")
    'hello'


