.. _frozensets:

Frozensets 
###########


.. contents::
       :depth: 2

:ref:`sets` are mutable, and may therefore not be used, for example, as keys in dictionaries.

Another problem is that sets themselves may only contain immutable (hashable) values, and thus may not contain other sets.

Because sets of sets often occur in practice, there is the **frozenset** type, which represents immutable (and, therefore, hashable) sets.

Quick Example
===================

::

    >>> a = frozenset([1, 2, 3])
    >>> b = frozenset([2, 3, 4])
    >>> a.union(b)
    frozenset([1, 2, 3, 4])


Set of Sets
==================

Sets may only contain immutable (hashable) values, and thus may not contain other sets, in which case frozensets can be useful. Consider the following example::

    >>> a = set([1, 2, 3])
    >>> b = set([2, 3, 4])
    >>> a.add(b)
    Traceback (most recent call last):
        File "<stdin>", line 1, in ?
            TypeError: set objects are unhashable
    >>> a.add(frozenset(b))



Using set as key in a dictionary
==================================

If you want to use a set as a key dictionary, you will need frozenset::

    >>> fa = {frozenset([1,2]): 1}    
    >>> fa[ frozenset([1,2]) ]
    1


Methods
==========

frozensets have less methods than sets. 

There are some operators similar to sets (:func:`intersection`, 
:func:`union`, :func:`symmetric_difference`, :func:`difference`, :func:`issubset`,
:func:`isdisjoint`, :func:`issuperset`) and a :func:`copy` method.
