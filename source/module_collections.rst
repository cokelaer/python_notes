.. _collections_module:

The collections module 
##################################



The :mod:`collections` module provides additional data structure. For now, we'll look at the :class:`deque` data structure. Consider also the OrderedDict class, which is similar to a dictionary but with keys being ordered. 


Deque: double-ended queues
=======================================

Double-ended queues, or deques, can be useful when you need to remove elements in the order in which they were added. You can find the deque functions in the **collections** module.

    >>> from collections import deque
    >>> q = deque(range(5))
    >>> q.append(5)
    >>> q.appendleft(6)
    >>> q #doctest: +SKIP
    deque([6, 0, 1, 2, 3, 4, 5])
    >>> q.pop()
    5
    >>> q.popleft()
    6
    >>> q.rotate(3)
    >>> q #doctest: +SKIP
    deque([2, 3, 4, 0, 1])


The reason for the usefulness of the deque is that it allows appending and popping efficiently
at the beginning (to the left), as opposed to lists. As a nice side effect, you can also rotate the
elements (that is, shift them to the right or left, wrapping around the ends) efficiently. Deque
objects also have extend and extendleft methods, with extend working like the corresponding
list method, and extendleft working analogously to appendleft. Note that the elements in the
iterable used in extendleft will appear in the deque in reverse order.


Named Tuples
=================

Sometimes, it is convenient to access to a mutable element by its names rather than an index. This is
possible with the :func:`collections.namedtuple` function. Your first need to design a structure using namedtuple  function. Then, you create the named tuple.

::

    person = collections.namedtuple("FirstName", "Surname", "age")
    persons = []
    persons.append(person("Alain", "Delon", 32))
    persons.append(person("Jean", "Gabin", 39))

You can now access to the first names of each tuple using the name attribute::

    first_names = [x.name for x in persons]

todo
========

collections.Callable         
collections.Iterable         
collections.MutableSet
collections.Container        
collections.Iterator         
collections.Counter          
collections.KeysView         
collections.OrderedDict
collections.defaultdict      
collections.Mapping          
collections.Sequence
collections.MappingView      
collections.Set
collections.Hashable         
collections.MutableMapping   
collections.Sized
collections.ItemsView        
collections.MutableSequence  
collections.ValuesView




