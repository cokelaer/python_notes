DATABASES in Python with dbm module
####################################


Python supports any DBM (database manager) and a similar interface. The main difference lies in the underrlying format. The database is a persistent dictionaries that work like normal Python dictionaries except that the data is written to and read from disk.

Amongst the different DBM, the **anydbm** module offers an alternative to choose the best DBM module available. If you need a very specific feature of another DBM module, use the **anydbm** module.

Quickstart with DBM
========================

Let us first create a database::

    >>> import anydbm
    >>> # open a DB. The c option opens in read/write mode and creates the file if needed.
    >>> db = anydbm.open('websites', 'c')
    >>> # add an item
    >>> db["item1"] = "First example"
    >>> print db['item1']
    "First example"
    >>> # close and save
    >>> db.close()

.. warning:: the key and value of each entry must be a string

