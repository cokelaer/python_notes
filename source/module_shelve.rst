.. _module_shelve:

The shelve module
######################


:Status: in progress


The :mod:`shelve` alloas you to store pickled objects (see :ref:`module_pickle` section) in a perseistent manner. It is useful to store large amount of data because Python performs shelf lookups as needed instead of loading the entire shelf in memory.

To open and create a shelf, type::

   import shelve
   s = shelve.open("storage", "c")

The first argument is the name of the file (without extension), and the second argument (the flag) can be *r* to open an existing shel in read-only mode, **w** to open a shelf in write mode, and **c** to open an existing database for read-write access (created if it does not exists); **n** can also be used to create a new database (for read-write acecss).

A shelf behaves like a dictionary but keys can be only strings and its values can be only objects that can be pickled. There are also a restricted numbers of dictionary operations available(e.g.,  has_key(), keys(), iteritems, get, ...).

You can call close() once you want to save the database or sync() to write unsaved data without closing the file.


what about s.cache and  s.writeback.


shelf contains Picklet and Unpickler functions. See :ref:`module_pickle`.

.. todo::

        shelve.BsdDbShelf        shelve.StringIO         shelve.UserDict
        shelve.DbfilenameShelf  shelve.Shelf           

