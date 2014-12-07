Iterators
################

We have already seen iterators in the previous sections. In this section, we will define more precisely what they are and how to make them.

Iterators are objects that can be traversed through all the elements of a collection. When you loop over a dictionary or a string or a list you use the iterator of the structure itself. For instance, if you loop over a dictionary you get its keys::

    >>> data = {"a":1,"b":2,"c":3}
    >>> for key in data:
    ...    print key
    a
    b
    c

Iterators have different behaviour depending on the object type. For instance, if you loop over a string, you get characters::

    >>>  s = "test"
    >>> for c in s:
    ...     print c
    t
    e
    s
    t

You can loop over a file as well and would get lines::

    >>> for line in open("test.data"):
    ...     print(line)

Many functions can take iterators as inputs (e.g., min, max, sum) as well as constructors (e.g., list, tuple, set, dict).

You can use constructors as well::

    >>> x = [1, 2, 3]
    >>> iterx = iter(x)
    >>> list(iterx)
    [1, 2, 3]

You can transform an object into an iterator using  the :func:`iter` builtin function::

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

When there is no more element to fetch, the StopIteration error is raised.

The iterator protocol: how to create iterator
------------------------------------------------

Objects that supports **iter()** and **next()** are said to be iterable. To do so you just need to implement the __iter__ and next() method.



::

    class CountDown(object):

        def __init__(self, start):
            self.count = start

        def __iter__(self):
            return self

        def next(self):
            if self.count <= 0:
                raise StopIteration
            r = self.count
            self.count -= 1
            return r


.. seealso:: :ref:`classes`


sentinel
-----------

iter() can take a callable argument. For instance::

    def seek_next_line(f):
        for c in iter(lambda: f.read(1),'\n'):
            pass

The iter(callable, sentinel) can be used in such a way that the callable is called until it returns the sentinel.


