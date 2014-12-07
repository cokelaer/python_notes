DATABASES in Python with dbm module
####################################
:Status: in progress

Python provides a database API that is very useful when needed to work with different type of databases. The data are stored within a DBM (database manager) persistent dictionaries that work like normal Python dictionaries except that the data is written to and read from disk.

There are many DBM modules that are unfortunately not compatible. Amongst them, the **anydbm** module offers an alternative to choose the best DBM module available. Except if you need a very specific feature of another DBM module, use the **anydbm** module.

Quickstart with DBM
========================

The following example illustrates the use of a DBM module that is used to store data into a DB using dictionary-like syntax.::

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


Python supports any DBM (database manager) and a similar interface. The main difference lies in the underrlying format. The database is a persistent dictionaries that work like normal Python dictionaries except that the data is written to and read from disk.

Amongst the different DBM, the **anydbm** module offers an alternative to choose the best DBM module available. If you need a very specific feature of another DBM module, use the **anydbm** module.


The DBM modules work when your data needs can be stored as key/value pairs. You can use such DBM persistent dictionary when :

* data needs are simple
* small amount of data
* if you require support for transactions (when more than one thing happens at once), use a relational database

Relational databases
====================


.. warning:: we assume that you know SQL commands. 

There are several databases possible. We will use sqlite3::

    >>> import sqlite3
    >>> conn = sqlite3.connect("example.db")
    >>> c = conn.cursor()
    >>> c.execute('create table Persons (id int, name text, city text)')
    >>> c.execute('insert into Persons VALUES (1, "smith", "dallas")')
    >>> conn.commit()
    >>> conn.close()


    >>> import sqlite3
    >>> conn = sqlite3.connect('example.db')
    >>> c = conn.cursor()
    >>> x = c.execute("select * from Persons")
    >>> x.fetchall() 
    [(1, u'smith', u'dallas')]

now fetchall is empty. You need to execute a command again 



MySQLdb
===========
.. warning:: Not a standard python module.  Not tested

::

    import MySQLdb
    connection = MySQLdb.connect(host="localhost", db="Student", port=8000, 
        username="laura", passwd="password")
    conn = connection.cursor()
    conn.execute('create table Login (user char(20),password char(20))')
    conn.execute('insert into Login values("user1","passwd2")')
    results = conn.execute('select * from Login')

    results.fetchone()
    results.fetchall()



todo
=====


cursor::

    x.arraysize      x.fetchmany      x.row_factory
    x.executemany    x.rowcount
    x.executescript  x.lastrowid      x.setinputsizes
    x.description  x.setoutputsize

connection using connect

    conn.DataError             conn.create_function
    conn.DatabaseError         conn.cursor
    conn.Error                 conn.execute
    con.IntegrityError        conn.executemany
    conn.InterfaceError        conn.executescript
    conn.InternalError         conn.interrupt
    conn.NotSupportedError     conn.isolation_level
    conn.OperationalError      conn.iterdump
    conn.ProgrammingError      conn.rollback
    conn.Warning               conn.row_factory
    conn.close                 conn.set_authorizer
    conn.commit                conn.set_progress_handler
    conn.create_aggregate      conn.text_factory
    conn.create_collation      conn.total_changes


