.. _buffering:



The buffer and memoryview builtin functions in details.
==========================================================


The buffers and memoryviews are efficient ways to deal with the
immutability of strings in Python, and the general copying behavior of slicing

The difference between memoryview and buffer is simple. An object created with memoryview can be is read/write whereas with buffer the object can only be read.

buffer
-----------

Let us consider a large string **S**. Let us assume that we want to split the
string into chumks of Nb bytes. One way to do it with list comprehension is::

    S2 = tuple( S[i*Nb:i*Nb+Nb] for i in range(0, len(S), Nb) )

This is fine as long as the input string is not too large. Indeed, each slice
creates its own copy. Another way to do this is to use the :func:`buffer`::

    S3 = tuple(buffer(S, i, Nb) for i in range(0, len(S), Nb))

The two iterators S2 and S3 would behave in the same way if we iterate over M as
follows::

    for this in S2:
        # do something with this variable
    for this in S3:
        # do something with this variable

However, the method with the :func:`buffer` function does it WITHOUT copying any
parts of the initial string.




buffer protocol 
--------------------

:Reference: http://eli.thegreenplace.net/2011/11/28/less-copies-in-python-with-the-buffer-protocol-and-memoryviews/

Let us consider this case where a file is opened in binary mode, which returns a
bytes object::

    f = open(FILENAME, 'rb')
    data = f.read()

bytes object are actually immutable so the following code (to change some data)
fails::

    data[0] = 1

So, we need to transform/cast the data (e.g., in bytearray)::

    f = open(FILENAME, 'rb')
    data = bytearray(f.read())
    data[0] = 1

good. That's whay we wanted. What is the  input file is large and we want to
repeat the task. How to optimise this code ? Indeed, there is an extra copy created when
data is instanciated. How to initialize the bytearray object without copying a temporary buffer ? With the :ref:`buffer` protocol.

There is actually a way using bytearray and hardly extra code which looks like::

    f = open(FILENAME, 'rb')
    data = bytearray(os.path.getsize(FILENAME))
    f.readinto(data)


This code uses the **buffer protocol**, which means that the __buffer__ method is
implemented in bytearray class and avoid extra copies. The buffer protocol is
used in the standard library (for example array.array and ctypes) and 3rd party libraries (
e.g., numpy).

How does that work ? The Python buffer protocol uses the producer consumer design 
pattern. The producer exposes its internals via the buffer protocol, and the
consumer accesses those internals.

Coming back to the previous example, a bytearray is created by pre-allocating the size of the data we’re
going to read. This pre-allocation is essential since readinto directly
accesses the internal buffer of bytearray. Next, the file.readinto method is used to read the data directly into
the bytearray’s internal storage, without going via temporary buffers.


The buffer implementation under the hood is in C and we will not cover this
aspect here. Have alook at the refernce if you are interested in this aspect.




memoryview
---------------

On writable producers such as bytearray, a
memoryview creates a writable view (can be modified)::

    >>> buf = bytearray(b'This is corpect')
    >>> mv = memoryview(buf)
    >>> mv[10:12] = 'rr'
    >>> buf
    bytearray(b'This is correct')

So, we can now read from a file directly in the middle of an existing buffer::

    buf = bytearray(...) # pre-allocated to the needed size
    mv = memoryview(buf)
    numread = f.readinto(mv[some_offset:])




