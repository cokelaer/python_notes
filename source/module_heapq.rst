.. _heapq_module:

The heapq module 
##################################

A priority queue lets you add objects in an arbitrary order and at any time (possibly in-between the adding) find (and possibly remove) the smallest element. It does so much more efficiently than, say, using *min* on a list.

The **heapq** module (with the q standing for queue) contains six functions, the first four of which are directly related to heap manipulation. You must use a list as the heap object itself.


The **heappush** function is used to add an item to a heap. Note that you shouldn't use it on
any old list--only one that has been built through the use of the various heap functions. The
reason for this is that the order of the elements is important.

    >>> from heapq import *
    >>> from random import shuffle
    >>> data = range(10)
    >>> shuffle(data)
    >>> heap = []
    >>> for n in data:
    ...     heappush(heap, n)
    >>> heap #doctest: +SKIP
    [0, 1, 3, 6, 2, 8, 4, 7, 9, 5]
    >>> heappush(heap, 0.5)
    >>> heap #doctest: +SKIP
    [0, 0.5, 3, 6, 1, 8, 4, 7, 9, 5, 2]


.. note:: The order of the elements isn't as arbitrary as it seems. They aren't in strictly sorted order, but there is one guarantee made: the element at position *i* is always greater than the one in position *i // 2*. This is the basis for the underlying heap algorithm. This is called the heap property.

The **heappop** function pops off the smallest element, which is always found at index 0, and
makes sure that the smallest of the remaining element takes over this position:

    >>> heappop(heap)
    0
    >>> heappop(heap)
    0.5
    >>> heappop(heap)
    1
    >>> heap #doctest: +SKIP
    [2, 5, 3, 6, 9, 8, 4, 7]

Note the method **heappushpop** that pushes item on the heap, then pops and returns the smallest item
from the heap. The combined action runs more efficiently than heappush() followed by a separate call to heappop().



The **heapify** function takes an arbitrary list and makes it a heap:
    
    >>> heap = [5, 8, 0, 3, 6, 7, 9, 1, 4, 2]
    >>> heapify(heap)
    >>> heap #doctest: +SKIP
    [0, 1, 5, 3, 2, 7, 9, 8, 4, 6]

The **heapreplace** function is not quite as commonly used as the others. It pops the smallest element off the heap and then pushes a new element onto it. This is more efficient than a heappop followed by a heappush:

    >>> heapreplace(heap, 0.5)
    0
    >>> heap #doctest: +SKIP
    [0, 0.5, 3, 4, 1, 6, 8, 9, 7, 5, 2] 
    >>> heapreplace(heap, 10)
    0.5
    >>> heap #doctest: +SKIP
    [1, 2, 5, 3, 6, 7, 9, 8, 4, 10] 
    
The remaining two functions of the heapq module, **nlargest(n, iter)** and **nsmallest(n, iter)**, are used to find the n largest or smallest elements, respectively, of any iterable object iter. You could do this by using sorting (for example, using the sorted function) and slicing, but the heap algorithm is faster and more memory-efficient (and, not to mention, easier to use).


Other Methods
==============

Like list, there is a :meth:`count` method to count occurences of an item.


todo
========


heapq.bisect       
heapq.izip         
heapq.repeat
heapq.chain        
heapq.imap         
heapq.merge        
heapq.tee
heapq.cmp_lt       
heapq.islice       
heapq.itemgetter       


