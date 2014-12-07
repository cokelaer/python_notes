.. _module_copy:


copy module
##################

:Status: in progress

The :mod:`copy` module implements shallow and deep copying operations.

How to copy a list
====================

Three ways::

    >>> l2 = list(l)
    >>> l2 = l[:]
    >>> import copy
    >>> l2 = copy.copy(l)

.. warning:: Don't do l2 = l, which is a reference, not a copy.


The preceding techniques for copying a list create *shallow copies*. IT means that nested objects will not be copied. Consider this example::


    >>> a = [1, 2, [3, 4]]
    >>> b = a[:]
    >>> a[2][0] = 10
    >>> a
    [1, 2, [10, 4]]
    >>> b
    [1, 2, [10, 4]]

To get around this problem, you must perform a deep copy::

    >>> import copy
    >>> a = [1, 2, [3, 4]]
    >>> b = copy.deppcopy(a)
    >>> a[2][0] = 10
    >>> a
    [1, 2, [10, 4]]
    >>> b
    [1, 2, [3, 4]]


