.. _data_structures:

Data Structures (list, dict, tuples, sets, strings)
######################################################

There are quite a few data structures available. The builtins data structures are: lists, tuples, dictionaries, strings, sets and frozensets.

Lists, strings and tuples are ordered sequences of objects. Unlike strings that contain only characters, list and tuples can contain any type of objects. Lists and tuples are like arrays. Tuples like strings are immutables. Lists are mutables so they can be extended or reduced at will. Sets are mutable unordered sequence of unique elements whereas frozensets are immutable sets.

Lists are enclosed in brackets::

    l = [1, 2, "a"]

Tuples are enclosed in parentheses::

    t = (1, 2, "a")

Tuples are faster and consume less memory. See :ref:`tuples` for more information.

Dictionaries are built with curly brackets::

    d = {"a":1, "b":2}

Sets are made using the :func:`set` builtin function. More about the data structures here below:

.. toctree::
    :maxdepth: 1

    lists.rst
    tuples.rst
    dicts.rst
    strings.rst
    sets.rst
    frozensets.rst


There are additional data structures available in the :ref:`collections <collections_module>` and :ref:`heapq <heapq_module>` modules for instance. 
