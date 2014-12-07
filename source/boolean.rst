.. _booleans:

Notes about booleans and logical operators
###########################################



The boolean type
==================

A boolean expression (or logical expression) evaluates to one of two states true or false. 
Python provides the boolean type that can be either set to **False** or **True**.
Many functions and operations returns boolean objects. 

The **not** keyword can also be used to inverse a boolean type.

    >>> not True
    False





What is False ?
=================

Every object has a boolean value. The following elements are false:

    * None
    * False
    * 0  (whatever type from integer, float to complex)
    * Empty collections: "", (), [], {}
    * Objects from classes that have the special method __nonzero__
    * Objects from classes that implements __len__ to return False or zero


Example of a class with type set to False::

    >>> class A():
    ...     def __len__(self):
    ...         return 0
    ...     
    >>> class B():
    ...     def __nonzero__(self):
    ...         return 0
    ...     
    >>> a = A()
    >>> bool(a)
    False
    >>> b = B()
    >>> bool(b)
    False

All other objects are True.


.. index:: and, or, is, not

Comparison  operators
========================

The <, <=, >, >=, ==, != operators compare the values of 2 objects and returns True or False. Comparison depends on the type of the objects. See the :ref:`classes` to see how to refedine the comparison operator of a type.

::

    10 == 10
    10 <= 10.


Chaining comparison operators
===================================

Comparison operators can be chained. Consider the following examples::

    >>> x = 2
    >>> 1 < x < 3
    True
    >>> 10 < x < 20 
    False
    >>> 3 > x <= 2
    True
    >>> 2 == x < 4
    True

The comparison is performed between each pair of terms to be evaluated. For instance in the first example, 
1<x is evaluated to True AND  x<2 is evaluated. It is not as if 1<x is evaluated to True and then True<3 is evaluated to True !!! 
Each term is evaluated once.



    
.. index:: not, and, in, or, not in

Evaluation of logical and comparison operators and membership operators
========================================================================

The evaluation using the **and** and **or** operators follow these rules:

* `and` and `or` evaluates expression from left to right. 
* with `and`, if all values are `True`, returns the last evaluated value. If any value is false, returns the first one.
* `or` returns the first `True` value. If all are `False`, returns the last value

=============== ===================================================
operators       descriptions
=============== ===================================================
not x           Returns True if x is True, False otherwise
x and y         Returns x if x is False, y otherwise
x or y          Returns y if x is False, x otherwise
=============== ===================================================

See :ref:`examples` for more details.

.. index:: in, not in, membership operator

Membership operators
=======================

* `in` evaluates to True if it finds a variable in a specified sequence and false otherwise. 
* `not in` evaluates to False if it finds a variable in a sequence, True otherwise.

.. doctest::

    >>> 'good' in 'this is a great example'
    False
    >>> 'good' not in 'this is a great example'
    True

The membership operator is a linear operator. It is therefore slow on list/tuple but fast of dictionary/set. 



.. index:: is, is not

Identity operators
===================
* `is` evaluates to True if the variables on either side of the operator point to the same object and False otherwise

* `is not` evaluates to False if the variables on either side of the operator point to the same object and True otherwise

.. doctest::

    >>> p = 'hello'
    >>> ps = p
    >>> ps is p
    True

Some data structure will not allow the comparison::

    obj == None

In which case, the identity operator may be used::

    obj is None

An example is the Pandas dataframe data structure.


.. index:: bitwise operators, cmp, >>, <<, ~, |, &, ^

Bitwise operators
=======================

Bitwise operators are used to compare integers in their binary formats.

When performing a binary operations between 2 integers, there are first converted into binary numbers. 
 
Let us show a few examples to explain the bitwise operations. The *and* operation between 2 the values 5 and 4 is actually the *and* operations between 1011 and 1001 binaries. It is therefore equal to 1001:

.. doctest:: 

     >>> cmp(4, 5)
     -1 


=========================== ====================================================
bitwise operators           descriptions
=========================== ====================================================
>>                          bitwise left shift
<<                          bitwise rightshift
&                           bitwise and
^                           bitwise xor
|                           bitwise or
~                           bitwise not
=========================== ====================================================

The left and right shifts can divide or multiply by power of 2 easily (integer conversion is made):

.. doctest::

    >>> 25 >> 2
    6
    >>> 25 << 2
    100

.. warning:: There is no overflow check. so if a right shift exceeds 2^31, the operation deletes extra bits and flips the sign.


The not operator works as follows:

.. doctest::

    >>> ~38
    -39
    >>> ~-38
    37

Order of evaluation
==========================

The order of evaluation from highest to order is as shown in this table:

=========================== ====================================================
operators                   descriptions
=========================== ====================================================
(), [], {}, ''              tuple, list, dictionnary, string
x.attr, x[], x[i:j], f()    attribute, index, slide, function call
+x, -x, ~x                  unary negation, bitwise invert
`**`                        exponent
`*`, /, %                   multiplication, division, modulo
+, -                        addition, substraction
<<, >>                      bitwise shifts
&                           bitwise and
^                           bitwise xor
|                           bitwise or
<, <=, >=, >                comparison operators
==, !=, is, is not, in,     comparison operators (continue)
not in                      comparison operators (continue)
not                         boolean NOT
and                         boolean AND
or                          boolean OR
lambda                      lamnda expression
=========================== ====================================================

Here is the precedence table for the boolean operators only


================ ==========================
operator
================ ==========================
`==`
`!=`
and
or
================ ==========================


.. index:: short-circuit

Boolean Examples
=====================

Short-circuit evaluations
---------------------------

To speed up boolean evaluations, Python uses **short-circuit** evaluations. It means that boolean evaluation may stop if one of its expression is False. For instance the following expression is always False ::

    False and X

and X is never evaluated.

Returned values
-------------------

In logical test, the returned value is the one that has been evaluated last. Consider these examples:

.. doctest::

    >>> print (True and "OK" or "KO")
    OK
    >>> print (False and "OK" or "KO")
    KO

:Explanation: in the first statement, ``True and "OK"`` is True. There is not need to test ``or "KO"``, so this is the end of the logical test, and the returned value is the one that has been evaluated last in ``True and "OK"``. In the second statement, ``False and "OK"`` is False. So, ``or "KO"`` must be evaluated. So, the last evaluated expression is ``"KO"``, hence the returned value.

precedence
-----------------

Consider::

    >>> True and False or True
   True

Since *and* has higer priority, the first evaluation is "True and False", which is always False. The second evaluation becomes therefore "False or True", which is True.

It maybe easier sometines to use brackets to make sure that what you wrote is what you meant::

    >>> (True and False) or True
    True



