
.. _introduction:

Quick Start / Tutorial 
###########################
:status: done
:Last reviewed: Dec 2014

This page is a quick introduction to the Python language. All aspects are covered in more details in other pages. 

.. contents::


The basics
===========

.. index:: indentation


Indentation
-------------

Before starting, you need to know that in Python, code indentation is an essential part of the syntax. It is used to delimitate code blocks such as loops and functions. It may seem cumbersome, but it makes all Python code consistent and readable. The following code is incorrect::

    a = 1
      b = 2

since the two statements are not aligned despite being part of the same block of statements (the main block). Instead, they must be indented in the same way::

    a = 1
    b = 2

Here is another example involving a loop and a function (def)::

    print("Here we are in the main script. No identation yet")

    def example():
        # The content of the function starts with an indentation including this comment
        for i in [1, 2, 3]:
            # The loop starts with an indentation as well
            print(i)

        print("End of the function")

    # call the function
    example()


.. index:: affectation, print

The print function (1): the Hello world
-----------------------------------------

In order to print the *Hello world* string, use the :func:`print` function as follows::

    >>> print("Hello world")
    Hello world

Note that before Python 3, you could use *print* without brackets::

    >>> print "Hello world"
    Hello world

More about printing later on.


.. index:: variable, type

Variables and Types (Toy example)
------------------------------------

In the remaining part of this quick introduction, we will play with a very simple example that consists in computing the surface of a circle. 

First, we need to use some variables. In python, there is no need to declare variables and therefore there is no need to declare type either. In Python, you hardly need to bother about types but you may need cast from time to time. For instance, the following lines declare a constant PI and a radius. There are both manipulated as float although we haven't mention it::

    pi = 3.14
    R = 1.


.. warning:: If you write ``R=1`` without a dot after the value, then its type is ``int``. Later, if you  need to cast it to a float, you can still use the :func:`float` function. This behaviour is true in Python 2 but has changed in Python 3.


Now, let us do the maths::

    surface = pi * R * R

or using the power sign::

    surface = pi * R**2

We can now print the content of the ``surface`` variable::

    >>> print(surface)
    3.14

.. index:: strings

Strings
--------

Of course, a more verbose message would be better but first, we need to show how to manipulate strings. In Python, they can be declared in 3 differents ways::

    message = 'The surface of the circle = '
    message = "The surface of the circle = "
    message = """The surface of the circle = """

In short, strings in double quotes work exactly the same as in single quotes but allow to insert single quote character inside them.
With the triple quotes (``'''`` or ``"""``), you can specify multi-line strings. Moreover, single quotes and double quotes can be used freely 
within the triple quotes.

It is easy to print non-homogeneous data types::

    >>> print(message , surface)
    The surface of the circle = 3.14


Here, notice the ``,`` sign. If the ``surface`` variable was a string, you could concatenate them using the ``+`` sign. 

.. note:: In Python, types are either mutable (can be changed) or immutable. Strings are immutable. For instance, message[0] = 'a' is not possible, although you can redeclare it: message = 'new text'. 


.. index:: print

The print function (2)
--------------------------

In order to print variables with :func:`print` function, as in many other languages (e.g., C) you will need the special character ``%``. Here we use only ``%s`` so every variables is casted to a string but you could use the standard symbols (e.g., %E, %d, ...).

::

    print('This is a circle of radius %s' % radius)
    print('This is a circle of radius %s and surface %s' % (radius, surface))

When using more than one argument, the print function requires to place the arguments in parentheses (this is a ``tuple`` as explained later).


.. index:: module, import


.. _basics_module:

Modules
=========

As soon as you want to start a project, you will need to copy your code into a file. In python, a file that contains Python code is called a **module** and it ends with the extension *.py*. You may notice files ending in *pyc*. Just ignore them. There are compiled files created by Python.

So, a module is just a file where functions and variables are available. 

Let us now come back to our toy example. As you may have noticed, the calculation of the surface will not be precise since we used only 2 digits to define the constant PI. Python has lots of standard modules amongst which the :mod:`math` module. To use a module within your own module, you need to **import** it::

    >>> import math

It contains lots a functions and constants and in particular the PI constant::

    >>> math.pi

Now, you can redo the computation and get a more precise value::

    surface = math.pi * R**2

Note that there are different ways to import modules or functions from a module. Instead of importing the entire math module, we could have imported only the PI value::

    from math import pi

which makes the syntax even simpler::

    surface = pi * R**2

If you want to import everything from a module, you can write::

    from math import *

You need to be cautious with this last statement. Indeed, you do not know what you are importing. You may have imported a function called ``surface`` that will 
overwrite you own variables or functions.

Note that the import statement can be placed anywhere in your code, however, the::

    import *

is forbidden within a class or function. It is allowed at module level only. 


See :ref:`docmodule` for more information about modules.



.. index:: function

Functions
==========

Now, that we know a little bit of Python syntax, it is time to create a re-usable function to compute the circle surface::

    from math import pi
    def compute_surface(radius, pi=math.pi):
        return pi* radius * radius

note the column at the end of the function declaration and the block indentation. This function has one argument and one optional argument (pi). You can call it as follows::

    surface1 = compute_surface(1., pi=3.14)
    surface2 = compute_surface(1.)

You can do much more of course (several outputs, variable number of arguments, ...) but that should be enough to start with in this page.

More about function in the :ref:`functions` section.

.. index:: sequences

Sequences (data structures)
==============================

There are lots of data structures in Python and sequences are of particular interest. Sequences allow to put together items that can be accessed to with indexing and slicing methods. You can find mutable and immutable sequences. 

.. note:: indices like in C starts at 0 (NOT 1)



.. index:: list

Lists
-------

Lists are mutable sequence. There are created using the square brackets.

::

    >>> radius_list = [1, 10.]
    >>> radius_list[0] 
    1

When you assign a variable the value of an existing object, Python makes a **reference** to the existing object. Consider te following example::

    >>> a = [1, 2, 3]
    >>> b = a
    >>> b[0] = 10
    >>> b
    [10, 2, 3]

a and b are two variables but they refer to the same object in memory. 



.. index:: tuple

Tuples
---------
Tuples are immutable sequence. There are created using the normal brackets.

::

    >>> radius_list = (1, 10.)
    >>> radius_list[0] 

.. index:: dictionary

Dicts
------

Dictionaries are mutable pairs of key/value. The key must be immutable type such as strings or numbers. There are defined using curly brackets.

::

    >>> d = {'key1': [1, 'e', 2, 'f', 'whatever'], 'key2':1}
    >>> d['key2']
    1


.. index:: strings

Strings
--------

Strings are sequences of characters. As already mentionned, there are immutable.

.. index:: slicing

Slicing
---------

Let us consider the following list:: 

    a = [1, 2, 3, 4]

that can be generated with the :func:`range` function::

    a = range(0, 4)

You can access to items in a sequences using an index (starting at zero)::

    >>> a[0]
    1


Note also that you can count down using negative indices::

    >>> a[-1]   # equivalent to a[3]
    4

You cannot use an index out of range. ``a[4]`` or ``a[-4]`` are wrong.

Slicing can be used to access to a sub list using this syntax::

    a[start:end:step]

If start is not provided, the default value is 0.
If end is not provided, the default value is the end of the sequence.
If step is not provided, the default value is 1.

An example would be to access the even values of a range::

    >>> range(1, 11)[::2]
    [0, 2, 4, 6, 8, 10]


summary
-----------

=============== =============== ==========
sequence        type            syntax
=============== =============== ==========
list            mutable         []
tuple           immutable       ()
dict            mutable         {}
string          immutable       ""
=============== =============== ==========


.. seealso:: :ref:`sets`, :ref:`frozensets`


.. index:: functional

Iterators
============

Iterators are objects that can be traversed through all the elements of a collection. In python many objects are iterators. The for loop (see next section) iterates through object(s). You can transform an object into an iterator using  the :func:`iter` builtin function 

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


.. seealso:: builtins


.. _functional:

Programming (and Functional programming)
===========================================

Python has the standard **loop** and **if** but also functional programming that are less standard (e.g., **list comprehension**).

.. note:: the apply, map and filter functions can be replaced by list comprehension.


.. index:: for, in, while, break, continue, membership operator

``for`` loop (and ``while``)
--------------------------------

You can loop over a sequence as follows::
 
    radius_list = [1., 10.,]
    for radius in radius_list:
        surface = compute_surface(radius)

Note again the indentation that delimits the scope of the loop. Hence, there is no need for an **end** keyword. The indentation suffices. Note also the way to iterate through the list using the **in** keyword (known as the membership operator). Any object that is an iterator (such as sequences) can be used in loops like in the example above. The  ``radius`` variable is created by the loop and therefore available within the loop. 


There is a **break** statement to stop the iteration of the loop/while loop. You may indeed face a situation in which you need to exit a loop when an external condition
is triggered. The break statement causes the program flow to exit the body of the while loop and resume the execution of the program at the next statement after the while loop. The break state-
ment can be used to force an early exit from a loop or to implement a loop with a test
to exit in the middle of the loop body. 

Example::

    >>> S = 0
    >>> while (S < 100):
    ...     S += (S+1)**2
    ...     if s > 100
    ...         break


Another keyword related to loops is the **continue** keyword. It returns the control to the beginning of the while loop. Instead of continuing the current iteration and then returning
the control to the beginning of the loop, the continue statement rejects all the remaining statements in the current iteration of the loop and moves the control back to the top
of the loop.




There is an optional ``else`` statement executed when the loop is over, which is hardly used but it is interesting to know its existence. It is not executed once the loop is finished (either normally or after a break statement):

.. doctest::

    >>> for i in [1,2,3]:
    ...    print(i)
    ... else: 
    ...    print "finished"
    1
    2
    3
    finished


builtin functions often used with the for loop are :func:`enumerate`, `range`, `xrange`. We've seen the range function earlier. xrange returns a generator instead of a list, which ,akes it slightly faster and memory more efficient. If you want to loop over a range and print the index you could write::

    count = 0
    for x in xrange(5,10):
        print(x, count)
        count += 1

but in python, you should use enumerate instead::

    for count, x in enumerate(xrange(5,10)):
        print(x,count)

 


Finally, the while loop works exactly as the for loop. Just replace ``for`` by ``while``. 

.. index:: if, in

``if`` condition
------------------

The following example illustrates the usage of if/elif/else keywords:


::

    radius_list = [1., 10., -1.]

    for radius in radius_list:
        if radius > 0:
            this_surface = compute_surface(radius)
            print "The surface of a circle of radius %s is %s" % (a_radius, this_surface)
        elif radius == 0:
            print 'There is no switch statement in Python, but you can use elif keyword as much as you want.'
        else:
            print "The radius is negative!"


.. note:: The special keyword **in** is a membership operator is used to find a variable in a sequence and can be used to loop over a sequence.

.. note::  `map` and `filter` can be very useful, and faster, but they were added to the language before list comprehension came along. Anything that map and filter can accomplish can also be done with list comprehensions:




do while loop
-------------------

There is no such loop in Python. Instead, you can use the **while**  loop (see above).


.. index:: pass

The pass statement
-----------------------

It is used when a statement is required but you do not want to do anything. Nothing happens when it is called. It is typically used in the init function of classes::

.. doctest::

    >>> class Test():
    ...     def __init__(self):
    ...         pass


.. index:: lambda

.. _lambda:

Lambda function
-----------------

In Python, lambda function can be used to replace a simple function. This lambda function is called an **anonymous** function because they have no name. 

To illustrate its syntax and usage, we start from the function defined earlier:

.. doctest::
    :options: +SKIP

    >>> from math import pi, sqrt
    >>> def compute_surface(radius)
    ...     return pi * radius * radius
    >>> compute_surface(sqrt(1./pi))
    1

An equivalent code using lambda function is:

.. doctest::
    :options: +SKIP

    >>> from math import pi, sqrt
    >>> f = lambda r: pi * r * r
    >>> f(sqrt(1./pi))
    1

You can use several parameters::

    >>> lambda x,y: return x**y


See :ref:`functions` for more details.

.. index:: zip

zip
----------

The :func:`zip` function takes one or more sequences as arguments and returns a list of tuples. The ith tuple contains the ith values of each sequence. If the input sequences do not have the same length, the list is truncated to the length of the shortest sequence. This function is often used to loop over several sequences::

    >>> for x,y in zip([1,2,3], [-1,-2,-3]):
    ...    print x+y
    0
    0
    0


.. index:: reduce

reduce
-------
The :func:`reduce` function is not very common but could be useful. It applies a function of two arguments cumulatively to the items of a sequence. The following example computes the factorial:

.. doctest::

    >>> reduce(lambda x, y: x*y, [1,2,3,4,5])
    120




.. index:: list comprehension

List comprehension
--------------------
In Python, there is a special syntax called ``list comprehension`` that allows to write loops in a very simple and intuitive way. Consider the following code:

.. doctest::
    :options: +SKIP

    >>> my_result = [] 
    >>> for radius in [1, 2, 3, 4]:
    ...     my_result.append(compute_surface(radius))

It returns the surface corresponding to radius in the list  ``[1,2,3,4]``. A list comprehension allows to rewrite this code in one line:

::

    my_results = [compute_surface(radius) for radius in [1, 2, 3, 4]]


So you can use list comprehension to create simple list. You can also include *if* condition::

    my_results = [compute_surface(radius) for radius in [0, 1, 2, 3, 4] if radius > 0]

You can have nested list comprehension. The following example flattens a nested lists::

    >>> nested = [[1, 2], [3, 4, 5]]
    >>> [x for s in nested for x in s]
    [1, 2, 3, 4, 5]

.. note:: if you have several for in a list comprehension keep in mind that the order of the for statements is the order you would expect them to be written in a standard for-loop (from the outside inwards).


Another example consist in building pairs from 2 lists::

    >>> s1 = [1, 2, 3]
    >>> s2 = [4, 5, 6]
    >>> [(x, y) for x in s1 for y in s2]
    [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]

    >>> [(x,y) for x in s1 for y in s2 if x+y>7]
    [(2, 6), (3, 5), (3, 6)]


You can also add if/else within a list comprehension as follows::

    [unicode(x.strip()) if x is not None else '' for x in row ]



List comprehension replaces the filter, map and apply functions in newer version of Python.

The next sections describe these 3 concepts. Their usage is not standard anymore but you may still encouter them in some old code or tutorials. If you are not interested, you can jump directly to the next section :ref:`exceptions_basics`.



.. index:: filter

filter
--------

The :func:`filter` function is often used with the lambda function. Its usage is::

    filter(function, sequence)

It returns the items of the sequence for which function(item) is true. For instance the following lambda function returns True if `x` is even::

    f = lambda x: x%2 == 0

which can be used within the filter

.. doctest::

    >>> f = lambda x: x%2 == 0
    >>> filter(f, [0,3,6,9])
    [0, 6]

In newer version of Python, list comprehension can be used to replace filter. The following statement are equivalent::

    >>> filter(func, seq)
    >>> [x for x in seq if func(x)]



.. index:: map

map
-----

Map is a special function for cases when you need to do a specific action on every element of a list. It enables you to accomplish this without having to write the loop. In newer version of Python map can be replaced by list comprehension but for book keeping, here is an example::

    >>> data = [ 'john', 'peter']
    >>> result = map(lambda x: "The name %s is %s letters long" % (x, len(x)), data)
    >>> print result
    ['The name john is 4 letters long', 'The name peter is 5 letters long']


.. index:: apply

apply 
--------

:func:`apply` is a function that takes as input a function, a tuple and a dictionary. It then calls the function given the tuple and dictionary as arguments. There is no need to use apply since in newer version of Python it is equivalent to calling a function as follows::

    func(*args, **kwargs)

where args is a tuple and kwargs a dictionary. See :ref:`functions`. 





.. index:: exceptions, try except

.. _exceptions_basics:

Exceptions
================

This section may not be for beginners anymore. You can code without knowing anything about Exception. However, you will see error messages for sure while playing with Python. Error messages are exceptions. 
In Python, there are many exceptions by default that can be used to catch errors. This is done using the try/except code blocks. Optional finally/else blocks may be used.

.. doctest::
    :options: +SKIP

    >>> try:
    ...     1./0.       # There is a ZeroDivisionError exception in Python
    >>> except ZeroDivisionError, e:
    ...     print 'Your own error message'
    ...     print e             # The ZeroDivisionError message
    >>> finally:
    ...     print 'The optional finally block always executes after the try/except blocks. '
    ...     # This is useful to close a file.
    >>> else:
    ...     print 'The optional else block is executed after the try block (if succeeded).'

If you do not know the type of error, you can use this syntax::

    >>> try:
    ...     1./0.
    >>> except e:
    ...     pass

See :ref:`exceptions` for more information about Exception, in particular user-defined exceptions.

.. index:: assert

Assert
=========


Asserts can be used to test the validity of some values::

    assert a > 0

You can add an error message:

.. doctest::

    >>> age = -1
    >>> assert 0 < age < 100, 'The age must be realistic'
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    AssertionError: The age must be realistic

.. warning:: you should use raise or exceptions instead of assert because the optimisation option of python ignores the assert statements.

.. index:: class

An object-oriented language
==============================

Python is an object oriented language. Everything is an object (list, generator, exception...).
Here is a very simple example that should help you starting with classes. Python offers most of the object-oriented tools that comes with other object-oriented languages from inheritance to operator overloading.

A class example
------------------
New class style should inherit from the **object** class.

.. code-block:: python

    class MyClass(object):

        # a class variable
        counter = 0

        # the constructor
        def __init__(self, arg1, arg2=0)
            self.arg1 = arg1
            self.__arg2 = arg2

        def a_method(self):
            print 'something'

        def __str__(self):
            return 'There are %s instances' % self.counter

Here, ``counter`` is a **class variable** shared by all instances whereas ``arg1`` is an **instance variable**. You then declare instances as follows::

    >>> c1 = MyClass(1)
    >>> c2 = MyClass(2, arg2=3)
    >>> print c1
    'There are 2 instances'
    >>> c2.counter 
    2.

.. note:: all class members (including the data members) are public and all the methods are virtual in Python.


If you use the double underscore prefix such as __arg2, Python uses name-mangling to make it a private variable.
However, you can still access to it if you want, so this is not a pure private data.


.. index:: inheritance

Inheritance
--------------

Here is an example of base and derived classes

.. code-block:: python

    class Tree(object):

        def __init__(self, name):
            self.name = name

        def __str__(self):
            return  'name: ' + self.name

    class FruitTree(Tree):

        def __init__(self, name, fruit_size)
            super(FruitTree, self).__init__(name)
            self.fruit_size = fruit_size

        def __str__(self):
            msg = super(FruitTree, self).__str__()
            msg += '\nIts fruit size is :'  + self.fruit_size


The inheritance is made thanks to the function **super**. Since functions are virtual the function __str__ in the Child class replaces the one defined in the Parent class.

See :ref:`classes` for a detailled overview of classes in Python.


Misc
=========

Single statement block
--------------------------

In general, a statement ends at the end of the line. There is no request for a special character such as semi column. However, you can use it if you want. The two following lines are equivalent::

    a = 1
    a = 1;

Of course, there is no interest to add a semi column in such case, which explain why you hardly see the semi column in Python code. However, you may want to write several statements on the same line::

    a = 1; b = 2

When a loop or if block statement is made of a single line, you may want to write it that way::

    if i > 0: print 1./float(i)


multiple assignment
------------------------

::

    >>> a, b, c = 1, 2, 3
    >>> a
    1    


Python shell
--------------------

In a shell, the underscore character retrieves the preceding result::

    >>> a = 5.1234
    >>> round(_, 2)
    5.12

comment
------------

use the ``#`` sign anywhere or quotes::

    >>> # this is a comment
    >>> a = 1 # another one
    >>> """ a very long comment ... 
    ... on several lines if needed"""

swapping element
-------------------

::

    x = 1
    y = 2
    x, y = y, x


None
-------

Python has a special type called None (e.g. equivalent to NULL in R). An example of None object is the object returned by a function that returns nothing. It is convenient to set a variable to an undefined values. 

Boolean
---------

Python has a boolean type. The False and True statement are coded as::

    >>> a = False
    >>> b= True
    >>> a == b
    False


See :ref:`booleans` for more details.

.. _int_div:

integer division
-----------------------

In python 2.x, the integer division may lead to unexpected results::

    >>> 5/2
    2

If you want the exact result, you should coerce to float::

    >>> 5/2.
    2


