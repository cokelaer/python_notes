
.. _sets:

Sets 
######


.. contents::
    :depth: 2


Sets are constructed from a sequence (or some other iterable object). Since sets cannot have duplicated, there are usually used to build sequence of unique items (e.g., set of identifiers).


Quick example
==================


::

    >>> a = set([1, 2, 3, 4])
    >>> b = set([3, 4, 5, 6])
    >>> a | b # Union
    {1, 2, 3, 4, 5, 6}
    >>> a & b # Intersection
    {3, 4}
    >>> a < b # Subset
    False
    >>> a - b # Difference
    {1, 2}
    >>> a ^ b # Symmetric Difference
    {1, 2, 5, 6}

.. note:: the intersection, subset, difference and symmetric difference can be be called with method rather that symbols. See below for examples.


Ordering
==========

Just as with dictionaries, the ordering of set elements is quite arbitrary, and shouldn’t be relied on.


Operators
============

As mentionned in the quick example section, each operator is associated to a symbol (e.g., &) and a method name (e.g. union).

 
    >>> a = set([1, 2, 3])
    >>> b = set([2, 3, 4])
    >>> c = a.intersection(b) # equivalent to c = a & b
    >>> a.intersection(b)
    set([2, 3])


    >>> c.issubset(a)
    True
    >>> c <= a
    True

    >>> c.issuperset(a)
    False
    >>> c >= a
    False

    >>> a.difference(b)
    set([1])
    >>> a - b
    set([1])

    >>> a.symmetric_difference(b)
    set([1, 4])
    >>> a ^ b
    set([1, 4])


You can also copy a set using the copy method::

    >>> a.copy()
    set([1, 2, 3])








