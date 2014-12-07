Variables, expressions, statements, types
##########################################

.. contents::


.. index:: variable

Naming variables
===================

Naming and naming conventions
---------------------------------

* Variable names are unlimited in length
* Variable names start with a letter or underscore *_* followed by letters, numbers or underscores.
* Variable names are case-sensitive
* Variable names cannot be keywords

Variable names conventionally have lower-case letters, with multiple words seprated by underscores. Classes use Camel style (words first letters are capitalised).

Variable names starting with underscore have a special meaning: when importing a module, variable that starts with underscore are not imported when typing::

    from mymodule import *

.. index:: keywords

keywords
----------------

Variable cannot be named after the keywords, which can be obtain easily using this code::

    >>> import keyword
    >>> keyword.kwlist

The list returned by this code is shown in the following table:

======= ========= ======= ========
======= ========= ======= ========
and     as        assert  break   
class   continue  def     del     
elif    else      except  exec    
finally for       from    global  
if      import    in      is      
lambda  not       or      pass    
print   raise     return  try     
while   with      yield
======= ========= ======= ========

Most of them are familiar if you already know some computer science but some may be knew (e.g., yield, lambda, import). You should find information about all these keywords in this document (use the search in the RHS).


Assignment (and multiple assignments)
=======================================

Assignment is done with the equal sign::

    x = 1
    y = 2

You can perform the same assignment on a single line with mulitple assignments::

    x, y = 1, 2

There is no limit on the number of multiple assignments but the number of variables and targets must be identical. Note the following statement, which is valid::

    >>> x, y, z = "ABC"
    >>> x, y, z
    ('A', 'B', 'C')

The string on the left has been split into 3 elements because its length is indeed 3, like the number of targets on the left.



It is also possible to assign a single value to multiple variables::

    >>> x, y, z = 0
    >>> x, y, z
    (0, 0, 0)


.. note:: when typing several variables separated by a comma, the returned object is a tuple (note the brackets). Similarly when returning several variables fro, a function. See :ref:`tuples` section.

.. index:: del
.. index:: reference counting

Deleting variables
=========================

Let us suppose assign to a variable *x* a simple object(list)::


    >>> x = [1, 2]

You can delete the variable *x* with the **del** keyword::

    >>> del x

Note, however that in python, you do not need to delete variables; it is done automatically. However, 
you can still do it for instance to delete a specific item in a list::

    >>> del x[0]
    >>> x
    [2]

.. note:: when you delete *x*, the object itself is not deleted since another variable may point to it. Python will delete the object itself once no variable refers to it anymore. This is done internally via reference counting 



.. index:: is, id
      
Determining an object's identity
==========================================

Every object has a unique identity that is constant over the lifetime of variable. Use the :func:`id` fu
nction to ::

    >>> x = "first"
    >>> y = x
    >>> id(x)
    123456
    >>> id(y)
    123456

Since *x* and *y* refer to the same object, they have the same *id*.
   
.. index:: type

Type of a variable
=========================

You can obtain the type of an object/variable by using :func:`type` function::

    >>> x = 1
    >>> type(x)
    <type 'int'>


In order to know the standard types provided by Python, use the :mod:`types` module and type::

    >>> import types
    >>> dir(types)
    ['BooleanType',
    'BufferType',
    'BuiltinFunctionType',
    'BuiltinMethodType',
    'ClassType',
    'CodeType',
    'ComplexType',
    ...


There are some aliases to the types in the module :mod:`types`. For instance when typing::

    >>> type("abc")
    str

you get the type of a string to be **str**::

    >>> type("abc") == str
    True

however, we can check that it is also the same type as **StringType** from the **types** module::

    >>> type("abc") == types.StringType
    True

Indeed, we can check that the two types are equivalent::

    >>> str == types.StringType
    True



.. index:: True, False, booleans, None

Boolean operators
=========================

Python provides the boolean type that can be either set to **False** or **True**.

In short, 0, **None** and empty sequences are False whereas non-empty objects are True.

More about boolean operators in :ref:`booleans`.


.. _manipulate_attribute:


.. index:: hasattr, delattr, setattr

Manipulating attributes
==========================

Python provides built-in functions that manipulate attributes. Let us play with the :mod:`math` module again.

    >>> import math
    >>> hasattr(math, 'pi')
    True 
    >>> getattr(math, 'pi') # equivalent to math.pi
    3.141592653589793
    >>> setattr(math, 'pi', 3.14)
    >>> getattr(math, 'pi')
    3.14
    >>> delattr(math, 'pi')
    >>> hasattr(math, 'pi')
    False

