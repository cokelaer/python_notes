.. _files:


Files
##############

Quick example
===============

In order to open a file (to read or to write), use the :func:`open` function::

    # here we use the write mode (w) to open a file to write in
    f = open('file.txt', 'w')
    f.write("something on a single line")
    f.close()

    # here we use the read-only mode (r) to read a file
    f = open('file.txt', 'r') # by default the mode is read-only
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line), # note the comma to avoid automatic new line
    f.close()


The mode can be 'w', 'r', 'a' for reading (default), writing or appending.  

The file will be created if it doesn't exist when opened for writing or appending; it will be truncated when
opened for writing.  Add a 'b' to the mode for binary files. Add a '+' to the mode to allow simultaneous reading and writing.

You can also provide a third argument for buffering. If ommitted (or 0), no buffer is used.; 1 means buffer one line at a time; larger numbers specify the buffer size.  

.. todo:: usage of **with**. 

Attributes
==========

The are attributes to access to the  ``name`` and ``mode`` of a file handler as well as its ``closed``::

    >>> f.name
    '/tmp/file.txt'
    >>> f.mode
    'w'
    >>> f.closed
    True


Methods to read a file
=========================

You can read a file line by line with ``readline``::

    >>> line = f.readline()

If EOF is reached, line is an empty string, which is False. So to read all the lines, you can type::

    >>> for line in f.readline()
    ...     # do something with line

If the file is not too large, you could read all the lines in one go to store them in a list::

    >>> lines = f.readlines()

Or you can read the entire file as a single string::

    >>> data =  f.read()

.. warning:: The newline character '\n' is included in all the line


Since files are also iterators, a fourth way to read a file is to iterate it::

    >>> for line in f:
    ...     print line, 


.. note:: the comma after the print statement is required. Indeed each line already contain the \n character. 


If your file is large, you can use the :meth:`file.xreadlines` function that use less memory than the **readline(s)** functions.
xreadlines returns the same list as readlines but it does not build the entire list at the same time, only when it is needed. 

To read only *N* characters, use an optional argument to the **read** function.

.. index:: writelines, flush, close

Methods to write  in a file
=============================

The write and writelines functions are the functions to be used to write in a file.
To write string in a file you should use :func:`write`. To write a list of strings, use :func:`writelines`.

::

    lst = ['a', 'b', 'c']
    f.writelines(lst)
    
    f.write("single string")

writelines does not qdd newlines at the end of each strings so you should add them yourself. You could do ::

    f.writelines([x+"\n" for x in lst])


Python performs buffering. So, data that you write may not actually appear in the file unless you can `f.flush` or `f.close` method. Any buffered data not yet written is written to the file when `flush` is called. Closing file is not stricly needed since Python closes files automatically when your script finishes. Hozever there are 2 good reasons to close files yourself: it saves memory and you will not write in the file by mistakes since a closed file cannot be manipulated anymore. 

.. index:: seek,tell

Changing position in a file
=============================
The :meth:`file.seek` Method is used to move the cursor position to different locations within a file.

The :meth:`file.tell` Method displays the current position of the cursor in a file from the start of the file. The first chracter is at position 0. 

    >>> f = open("temp.txt", "w")
    >>> f.write("first line\n")
    >>> f.write("second line\n")
    >>> f.write("third line\n")
    >>> f.close()
    >>> f = open("temp.txt", "r")
    >>> f.tell()
    0
    >>> f.readline()
    'first line\n'
    >>> f.tell()
    11

Now you can rewind back to the beginning of the file with :meth:`file.seek`:

    >>> f.seek(0)
    >>> f.readline()
    'first line\n'

The argument can be set to 0 as above, or 1 to use the current position or 2 to use the end of the file as the reference position.

.. index:: truncate, readline

Other methods
====================

There a are few other methods available when manipulating files. 

You can truncate a file but you must open as read/write::

    >>> f = open("temp.txt", "r+") 
    >>> f.readline()
    >>> f.tell()
    11
    >>> f.truncate(11)

Files have the iteratr method implemented, so meth:`file.next` returns the next value from a file. It is equivalent to :meth:`file.readline`.

You can also get file information using :meth:`file.fileno` to obtain the file descriptor, zhich is used at low-level file operations.

The :attr:`file.softspace` is used to indicate whether a space character needs to be printed before another value when using the print statement. You should not use it unless you want to implement a type in C language where you will have to provide the softspace attribute.

The :meth:`file.isatty` method returns True if the file is connected to a tty device.

The encoding that a file uses is stored in :attr:`file.encoding`. When Unicode strings are written to a file, they will be converted to byte strings using this encoding. 

Finally, there is a unicode error handler used along the encoding that is stored in :attr:`file.errors`
   

.. index:: fdopen

Other way to open files
==============================

You can play with the :mod:`os` module with :func:`os.fdopen`, popen, tmpfile, popen2, popen3, popen4 functions. See :ref:`os_module`





