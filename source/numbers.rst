.. _numbers:

Nearly everything about numbers
####################################

.. index:: float, complex, int, long, hex, oct

The numeric types
======================

There are 4 numeric types:

 * plain integers
 * long integers
 * floating-point numbers 
 * complex numbers

The long integers are code with the letter L::

    >>> 2**62
    4611686018427387904
    >>> 2**63
    223372036854775808L

To determine the largest possible integer on your system, use::

    >>> import sys
    >>> sys.maxint

Complex numbers are coded using the *j* letter for imaginary part::

    >>> a = 1 + 2j
    >>> a.real
    1.0
    >>> a.imag
    2.0
    >>> a.conjugate()
    (1 - 2*j)

Note that the type of the real and imaginary parts are floats becuase complex numbers use floats.


.. note:: :mod:`cmath` module provides the complex functions found in the :mod:`math` module


You may also use *octal* and *hexadecimal* integers. Octal starts with a zero, and hexadecimal with zero and x::

    >>> 010
    8
    >>> 0xa
    10


You can use :func:`hex` and :func:`oct` to convert an integer number to an hexadecimal or octal string::

    >>> hex(10)
    '0xa'

.. seealso:: :func:`float.hex`.



Promotion
============


When you mix numeric types in an expression,  all operands are converted (or coerced) to the most complex type used in the expression::

    >>> 5 + 3.0
    8.0

The rules for promotion are 

#. if an operand is complex, the other is converted to a complex number
#. otherwise, if an operand is a float, the other is converted to a complex number
#. otherwise, if an operand is a long, the other is converted to a long
#. otherwise, the two operands must be integers.


You can use the :func:`coerce` function to check how the promotion will be done::

    >>> coerce(1, 2.0)
    (1.0, 2.0)


Be careful when divided integers. Indeed, in Python 2.x, the returned value is the quotient. So::

    >>> 5/2
    2

returns 2, not 2.5 as expected.

Conversion
=============

Although Python performs conversion internally, you can perform conversion explicitely. Thid can be done with :func:`int`, :func:`float`, :func:`complex`, :func:`long` but also :func:`oct` and :func:`hex`.



Remainder and quotient of a division
======================================

The % (modulo) and / signs returns the remainder and quotient of a division::

    >>> 5 % 2
    1
    >>> 5 / 2
    2

Alternatively, you can use :func:`divmod` function::

    >>> divmod(5, 2)
    (2, 1)

You can use the % sign fo integer but also float numbers::

    >>> 2.2 % 0.7
    0.1

Bit operations
==================


    >>> #inverts the bits
    >>> ~10
    -11 
    >>> # shift
    >>> 8 >> 2
    2
    >>> # shift
    >>> 2 << 2
    8
    >>> 1&0
    0
    >>> 1 | 0
    1
    >>> 1 ^ 1
    0


Raising a number to a power
==============================

Just use the ** symbol::

    >>> 2**2
    4


you can also use th function :func:`pow` to raise a power as well.

.. doctest::

    >>> pow(2,3)
    8

You can provide a third argument (mod) so the answer is the remainder of the reuslts  divided by the optional argument::

    >>> pow(2,3,5)
    3 



Augmented assignment operators
======================================


The augmented assignment operator are available for the following operator: +, -, `*`, /, `**`, %.

    >>> x = 1
    >>> x += 1
    >>> x
    2

More Maths
===========

So far, we've seen mathematical operators but no functions. Python provides a few built-in functions to perform more mathematical calculations. Examples are:

    :func:`abs`, :func:`cmp`, :func:`max`, :func:`min`, :func:`round`

Let us quickly present the round function that takes an argument to specify which digit to round::

    >>> round(33.49,1)
    33.5
    >>> round(33.49,-1)
    30.0


In addition you can use the :mod:`math` and :mod:`cmath` modules (cmath is the complex version of math). Finally, there is also a :mod:`random` module. See :ref:`modules` for more details. 


NaN and Inf
==============

    >>> float('Inf')
    inf
    >>> float('Inf')  + 1
    inf
    >>> float('NaN')
    nan
    >>> float('NaN') + 1
    nan




