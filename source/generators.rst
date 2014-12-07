.. _generators:

Generators
#############

A **Generator** is a function that produces a sequence of results instead of a single value (using the yield statement). The main interest of generators compared to a normal function is to avoid the creation of a list and therefore improve performance (memory-wise). 

Keep in mind that a generator is quite different from a normal function. Calling a generator function creates an object: it does not start running any statements.

The *quick example* below illustrates the interest of generators. The following sections gives more insight on where and when to use them.



.. contents::


.. index:: xrange, range, generator, yield

Quick example
================

Let us take an example. The builtins :func:`range` function generates a list from a low value to a high value. What if we want a symmetric range that goes from a low value to a high value and then to the low value again. With a standard function, we would write:

.. doctest::

    >>> def symrange(low, high):
    ...     a = range(low, high)
    ...     b = range(high-2, low-1, -1)
    ...     a.extend(b)
    ...     return a
    >>> a = symrange(0,3) 
    >>> a
    [0, 1, 2, 1, 0]

.. note:: xrange is the generator version of range but here we need to use range.

Here, *symrange(0,3)* returns a list, that may be used in a for loop later on.
What would happen if the symrange is made of million of points. Well, a lot of memory for nothing really special. Here comes the generator: 

.. doctest::

    >>> def symrange(low, high):
    ...     for a in xrange(low, high):
    ...         yield a
    ...     for b in xrange(high-2, low-1, -1): 
    ...         yield b
    >>> a = symrange(0,3)   # doctest: +SKIP
    <generator object symrange at 0xaaa65cc>

The **yield** produces a value but suspends the function. The function resumes on next call to next() function.

    >>> ite = symrange(0,10)
    >>> ite.next()
    0

You can call :meth:`next` until the generator returns. When it returns, the StopIteration error is returned.

So, generators can be used efficiently within a loop (the StopIteration is caught by the for loop)::

    >>> sym = symrange(0,3)
    >>> for x in sym:
    >>>    print x


.. index:: generator, lazy-evaluation, yield

Explanations
----------------

**Generators** are functions that contain the special word **yield**. They consist of two separate components: 

    1. the generator-function that is what is defined by the def statement containing a yield
    2. the generator-iterator that is what this function returns (the variable *sym* in the above example).

**Generators** behave quite differently from the ordinary function. The difference is that instead of returning one value, as you do with `return`, you can yield several values, one at a time. Each time a value is yielded (with yield), the function freezes: it stops its execution. When called again, it resumes its execution at the point where it stopped.

The main consequence is that the generator-built iterator is more efficient that the equivalent function in a memory point of view. Indeed, the generator performs a lazy-evaluation.




Sending values into generator functions
==========================================

Sending values into generator functions is possible by using the :meth:`send` method. Let us start with the following function (generator)::

    def mygen():
        """Yield 5 until something else is passed back via send()"""
        a = 5
        while True:
            f = (yield a) #yield a and possibly get f in return
            if f is not None: 
                a = f  #store the new value

You can then use it as follows::

    >>> g = mygen()
    >>> g.next()
    5
    >>> g.next()
    5
    >>> g.send(7)  #we send this back to the generator
    7
    >>> g.next() #now it will yield 7 until we send something else
    7

Although this example implements a function that is similar to a variable. However, the feature could be used in many other ways ... unlike a variable. It should also be obvious that similar semantics can be implemented using objects (a class implemting Python's call method, in particular



Generator version of a list comprehension
====================================================

You can create a generator using the brackets::

    x = (n for n in foo if bar(n))

x is a generator. It means you can type::

    for n in x:
    ...

The advantage of this is that you don't need intermediate storage, which you would need if you did::

    x = [n for n in foo if bar(n)]

In some cases this can lead to significant speed up. 


Generator and iterator
=========================

A generator function may be used to replace an iterator, which is convenient since there is no need for next or __iter__ method.

Note that a generator function is a one-time operation. You can iterate through the generated data but to do it again you need another generator.


Generator expression
========================


::

    (expression for i in s if cond1
                for j in t if cond2
                ...
                if conditional)

it means::

    for i in s:
        if cond1:
            for j in t:
                if cond2:
                    ...
                    if condfinal: yield expression



Performance of generators
============================   

 
An example provided in the reference consists in scanning a large log file, getting the last column and computing the sum. The last column may an integer or the "-" character that we need to reject with a condition. A classical way is to use a simple for-loop ::

    data = open("log.txt")
    total = 0
    for line in data:
        col = line.rsplit(None, 1)[1]
        if col != '-':
            total += int(col)

A generator version would look like::

    data = open("log.txt")
    bytecolumn = (line.rsplit(None, 1)[1] for line in data)
    bytes = (int(x) for x in bytecolumn if x!= "-")    
    total = sum(bytes)

On a 1.3Gb log file, the generator version appears to be 5% faster. Not a bit difference but still faster and more importantly at no time a large list has been created so it can be applied to large files and is competitive with traditional tools (twice as fast as a awk version). An example of generator that searches through a entire file system is the os.walk (see :ref:`os_module`)

Examples
==============

find
----------

A python equivalent of the unix **find** function (find . -name "*.py")
::

    import os
    import fnmatch

    def gen_find(filepat, top):
        for path, dirlist, filelist in os.walk(top):
            for name in fnmatch.filter(filelist, filepat):
                yield os.path.join-path, name)

    for name in gen_find("*.py", "."):
        print name

The unix version is faster but difference is only about 15% and you now have a find function on every platform !


flatten
--------------

Let us take an example. We want to flatten the following nested list:

.. doctest::

    >>> nested = [[1, 2], [3, 4], [5]]

Such a generator would do the job:

.. doctest::
       
    >>> def flatten(nested):
    ...     for sublist in nested:
    ...         for element in sublist:
    ...             yield element
    >>> list(flatten(nested))
    [1, 2, 3, 4, 5]








Some references
====================

* http://www.dabeaz.com/generators/Generators.pdf
