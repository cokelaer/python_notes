Notes about sorting lists and dictionaries
############################################



Sorting lists
===============

Let us remind the usage of the inline sorting method :meth:`~list.sort`:

.. doctest::

    >>> l = [1,4,2,9,3]
    >>> l.sort()
    >>> print l
    [1, 2, 3, 4, 9]

No surprise here. Now, let us mix non homogeneous data:

.. doctest::

    >>> l = ["B", 1, 4, 2, "a"]
    >>> l.sort()
    >>> print l
    [1, 2, 4, 'B', 'a']

**Here, data are ordered by types and then ordered between same types**. The type order cannot be logical, so be careful here. For instance upper case appear before lower case. So the ``'B'`` is before ``'a'``.


The big interest of list sorting is that you can specify your own method. Imagine that you do not bother about upper and lower case. The standard sorting method would not suffice. Instead, you would provide another function as follows: 

.. doctest::

    >>> l = ['a', 'B', 'A', 'b']
    >>> l.sort()
    >>> print l
    ['A', 'B', 'a', 'b']
    >>> l.sort(lambda x,y: cmp(x.lower(), y.lower()))
    >>> print l
    ['A', 'a', 'B', 'b']

where the lambda function alterates the normal behaviour of the ``cmp`` function by forcing the two inputs to be lower case. Of course the lambda function can be replaced by an external function.

In fact, this simple example could have use the key argument because strings have already the method lower available::

    
    >>> l = ['a', 'B', 'A', 'b']
    >>> l.sort(key=str.lower)
    >>> print l
    ['A', 'a', 'B', 'b']

list of dictionaries
=====================

If the list is made of items (like in a dictionary), the list will be sorted by key then by value:

.. doctest::

    >>> l = [ {'a':2} , {'c':1} , {'a':1}]
    >>> l.sort()
    >>> print l
    [{'a': 1}, {'a': 2}, {'c': 1}]

With list of dictionaries, you can sort using one particular key using the getitem method of the operator module, by selecting a specific key::

    l = [{'id':1, 'name':john}, {'id':10, 'name':'tom'}, {'id':3, 'name':'peter'}]
    l.sort(key=operator.itemgetter('id'))
    print l
    l = [{'id':1, 'name':john}, {'id':3, 'name':'peter'}, {'id':10, 'name':'tom'}]
