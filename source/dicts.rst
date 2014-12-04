.. index:: dict, keys, values, iterators, clear, setdefault, fromkeys

Dicts 
######


.. contents::
    :depth: 2


Quick example
==================

A dictionary is a sequence of items. Each item is a pair made of a key and a value.
Dictionaries are not sorted. You can access to the list of keys or values independently.

::


    >>> d = {'first':'string value', 'second':[1,2]}
    >>> d.keys()
    ['first', 'second']
    >>> d.values()
    ['string value', [1, 2]]

You can access to the value of a given key as follows::

    >>> d['first']
    'string value'


.. warning:: You can not have duplicate keys in a dictionary
.. warning:: dictionary have no concept of order among elements


Methods to query information
==============================

In addition to **keys** and **values** methods, there is also the **items** method that returns a list of items of the form (key, value). The items are not returned in any particular order::

    >>> d = {'first':'string value', 'second':[1,2]}
    >>> d.items()
    [('a', 'string value'), ('b', [1, 2])]

The **iteritems** method works in much the same way, but returns an iterator instead of a list. See :ref:`iterators` section for an  example.

You can check for the existence of a specific key with **has_key**::

    >>> d.has_key('first')
    True

The expression **d.has_key(k)** is equivalent to **k in d**. The choice of which to use is largely a matter of taste.


In order to get the value corresponding to a specific key, use **get** or **pop**::

    >>> d.get('first')  # this method can set an optional value, if the key is not found
    'string value'

It is useful for things like adding up numbers::

    sum[value] = sum.get(value, 0) + 1

.. seealso:: setdefault, :mod:`collections`

The difference between **get** and **pop** is that **pop** also removes the corresponding item from the dictionary::

    >>> d.pop('first')
    'string value'
    >>> d
    {'second': [1, 2]}

Finally, **popitem** removes and returns a pair (key, value); you do not choose which one because a dictionary is not sorted ::

    >>> d.popitem()
    ('a', 'string value')
    >>> d
    {'second': [1, 2]}

Methods to create new dictionary
=================================

Since dictionaries (like other sequences) are objects, you should be careful when using the affectation sign::

    >>> d1 = {'a': [1,2]}
    >>> d2 = d1
    >>> d2['a'] = [1,2,3,4]
    >>> d1['a]
    [1,2,3,4]

To create a new object, use the **copy** method (shallow copy)::

    >>> d2 = d1.copy()

.. seealso::  :func:`copy.deepcopy`

You can clear a dictionary (i.e., remove all its items) using the :meth:`clear` method::

    >>> d2.clear()
    {}


The :func:`clear` method deletes all items whereas :func:`del` deletes just one:

.. doctest::

    >>> d = {'a':1, 'b':2, 'c':3}
    >>> del d['a']
    >>> d.clear()


Create a new item with default value (if not provided, None is the default)::

    >>> d2.setdefault('third', '')
    >>> d2['third']
    ''

Create a dictionary given a set of keys::


    >>> d2.fromkeys(['first', 'second'])

another syntax is to start from an empty dictionary::

    >>> {}.fromkeys(['first', 'second'])
    {'first': None, 'second': None}


Just keep in ,ind thqt the :func:`fromkeys` method creates a new dictionary with the given keys, each with a default corresponding value of None.
    


Combining dictionaries
--------------------------

Given 2 dictionaries d1 and d2, you can add all pairs of key/value from d2 into d1 by using the update method (instead of looping and assigning each pair yourself::

    >>> d1 = {'a':1}
    >>> d2 = {'a':2; 'b':2}
    >>> d1.update(d2)
    >>> d1['a']
    2
    >>> d2['b']
    2

The items in the supplied dictionary are added to the old one, overwriting any items there
with the same keys.

.. _iterators:

iterators
===========

Dictionary provides iterators over values, keys or items::


    >>> [x for x in t.itervalues()]
    ['string value', [1, 2]]
    >>> 
    >>> [x for x in t.iterkeys()]
    ['first', 'csecond']
    >>> [x for x in t.iteritems()]
    [('a', 'string value'), ('b', [1, 2])]

.. seealso:: :ref:`builtins_iterator`

Views
======

**viewkeys**, **viewvalues**, **viewitems** are set-like objects providing a view on D's keys, values or items.



comparison
=================

you can compare dictionaries! Python first compares the sorted key-value pairs. It first sorts  dictionaries by key and comapre their initial items. If the items hae different values, Python figures out the comparison between them. Otherwise, the second items are compared and so on.


 
