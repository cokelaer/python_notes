Porting code to Python 2 and 3
######################################

:sources: 
    - http://python3porting.com/differences.html
    - http://www.diveintopython3.net/porting-code-to-python-3-with-2to3.html

The following contains only parts of the link above. The original 
link is really complete. This part contains only a subset of the
original version (relevant for the migration required on my packages). 
Besides, text has been simplified so for full details, please see the original 
link above.


Main differences
=================

Deprecated/Removed
--------------------

* apply()
* cmp() see later




buffer()
-----------

The Python 2 buffer() builtin is replaced by the memoryview class in Python 3. 
When function are replaced, the following template would do the trick::

    >>> import sys
    >>> if sys.version > '3':
    ...     buffer = memoryview
    >>> b = buffer('yay!'.encode())
    >>> len(b)
    4

callable()
----------------

The Python 2 builtin callable() was removed in Python 3.0, but reintroduced in Python 3.2. 

If you need to know if something is callable without calling it, there are several solutions for Python 3::

    >>> def afunction():
    ...     pass

    >>> any("__call__" in klass.__dict__ for 
    ...     klass in type(afunction).__mro__)
    True

    >>> import collections
    >>> isinstance(afunction, collections.Callable)
    True

If you need code that runs in both Python 2 and Python 3 you can use this::

    >>> hasattr(bool, '__call__')
    True


Classes
---------

In Python 2 there is two types of classes (old-style and new-style). The old-style classes have been removed in Python 3.
All classes now subclass from object, even if they don’t do so explicitly. In Python 2, just use an explicit declaration::

    class MyClass(object):
        pass


Comparisons
--------------

The Python 2 builtin cmp() has been removed in Python 3.0.1. Should you need cmp(), define it as::

    def cmp(a, b):
        return (a > b) - (a < b)


Dictionary methods
----------------------

In Python 2 dictionaries have the methods iterkeys(), itervalues() and iteritems() that return iterators instead of lists. In Python 3 the standard keys(), values() and items() return dictionary views, which are iterators, so the iterator variants become pointless and are removed.

If you need to support both Python 2 and Python 3 without 2to3 conversion and you must use the iterator methods, you can access it via a try/except::

    >>> d = {'key1': 'value1',
    ...      'key2': 'value2',
    ...      'key3': 'value3',
    ... }


    >>> try:
    ...     values = d.itervalues()
    ... except AttributeError:
    ...     values = d.values()


    >>> isinstance(values, list)
    False

    >>> for value in values:
    ...     print(value)
    value3
    value2
    value1

Also, the has_key() method on dictionaries is gone. Use the in operator instead.

except
---------

In Python 2 the syntax to catch exceptions have changed from::

    except (Exception1, Exception2), target:

to the clearer Python 3 syntax::

    except (Exception1, Exception2) as target:


Exception objects
-------------------

In Python 2 the exception object is iterable and indexable.
In Python 3 you must use the args attribute, which will work under Python 2 as well::

    >>> e = Exception('arg1', 'arg2')
    >>> e.args[1]
    'arg2'
    >>> for a in e.args:
    ...   print a
    ... 
    arg1
    arg2

exec
--------

In Python 2 exec is a statement. In Python 3 exec is a function::

    >>> g_dict={}
    >>> l_dict={}
    >>> exec("v = 3", g_dict, l_dict)
    >>> l_dict['v']
    3

The Python 3 syntax without the global and local dictionaries will work in Python 2 as well.


file
----

In Python 2 there is a file type builtin, which is replaced with various file types in Python 3. 
If you need to test for types you can in Python 3 check for io.IOBase instead of file.


Imports
--------------


In Python 2, if you have a package called mypackage and that contains a module called csv.py, it would hide the csv module from the standard library. The code ::

    import csv 
    
would within mypackage import the local file, and importing from the standard library would become tricky.

In Python 3, this has changed so that **import csv** would import from the standard library, and to import the local csv.py file you need to write::

    from . import csv 
    
and ::

    from csv import my_csv 
    
needs to be changed to ::
    
    from .csv import my_csv. 
    
    
These are called **relative imports**, and there is also a syntax to import from one level up module above: from .. import csv.

If you wish to support both Python 2 and Python 3, the from . and from .. syntax is available since Python 2.5, with a from __future__ import absolute_import statement that changes the behavior to the Python 3 behavior.


input() and raw_input()
-----------------------

In Python 2 there is raw_input() that takes a string from stdin and input() that takes a string from stdin and evaluates it. That last function is not very useful and has been removed in Python 3, while raw_input() has been renamed to input().

If you need to evaluate the input string you can use eval()::

    >>> eval(input('Type in an expression: '))
    'Type in an expression: ' 1+2
    3

If you need code that runs in both Python 2 and Python 3, you can  set input() to be raw_input()::

    >>> try:
    ...     input = raw_input
    ... except NameError:
    ...     pass


Integer division
----------------------


In Python 2, the result of dividing two integers will itself be an integer; in other words 1/2 returns 0. In Python 3 integer division will return an integer only if the result is a whole number. So 1/2 will return 0.5.

If you want the old behavior you should instead use the floor division operator //, available since Python 2.2. If you need to support both Python 2 and Python 3 without 2to3 conversion the following __future__ import works since Python 2.2 and enables the new behavior::

    >>> from __future__ import division
    >>> 1/2
    0.5

See also: Use // instead of / when dividing integers

long
-----------

Python 2 has two integer types int and long. These have been unified in Python 3, so there is now only one type, int. If you do need that in both Python 2 and Python 3, the following code works::

    >>> import sys
    >>> if sys.version > '3':
    ...     long = int
    >>> long(1)
    1L

However, the representation is still different, so doctests will fail. If you need to check if something is a number you need to check against both int and long under Python 2, but only int in Python 3. Use::

    >>> import sys
    >>> if sys.version < '3':
    ...     integer_types = (int, long,)
    ... else:
    ...     integer_types = (int,)
    >>> isinstance(1, integer_types)
    True



.next()
---------

In Python 2 you get the next result from an iterator by calling the iterators .next() method. In Python 3 there is instead a next() builtin.

If you need code that runs in both Python 2 and Python 3 without 2to3 conversion you can make a function that under Python 2 calls iterator.next() and under Python 3 calls next(iterator). The six module contains such a function, called advance_iterator().


Parameter unpacking
---------------------------

In Python 2 you have parameter unpacking::

    >>> def unpacks(a, (b, c)):
    ...     return a,b,c

    >>> unpacks(1, (2,3))
    (1, 2, 3)

Python 3 does not support this, so you need to do your own unpacking::

    >>> def unpacks(a, b):
    ...     return a,b[0],b[1]
    
    >>> unpacks(1, (2,3))
    (1, 2, 3)


print
-------

Just use print() all the time

=========================   =====================
Python 2                    Python3
=========================   =====================
print                       print()
print 1                     print(1)
print 1, 2,                 print(1, 2, end=' ')
print >>sys.stderr, 1, 2    print(1, 2, file=sys.stderr) 
=========================   =====================


raise
-------

In Python 2 the syntax for the raise statement is::

    raise E, V, T

Where E is a string, an exception class or an exception instance, V the an optional exception value in the case that E is a class or a string and T is a traceback object if you want to supply a traceback from a different place than the current code. In Python 3 this has changed to::

    raise E(V).with_traceback(T)

As with the Python 2 syntax, value and traceback are optional. The syntax without the traceback variable is::

    raise E(V)

This works in all versions of Python. It’s very unusual that you need the traceback parameter, but if you do and you also need to write code that runs under Python 2 and Python 3 without using 2to3 you need to create different a function that takes E, V and T as parameters and have different implementations under Python 2 and Python 3 for that function. 


range() and xrange()
------------------------

In Python 2 range() returns a list, and xrange() returns an object that will only generate the items in the range when needed, saving memory.

In Python 3, the range() function is gone, and xrange() has been renamed range(). In addition the range() object support slicing in Python 3.2 and later .


Rounding behavior
-------------------

The behavior of round has changed in Python 3. In Python 2, rounding of halfway cases was away from zero, and round() would always return a float.::

    >>> round(1.5)
    2.0
    >>> round(2.5)
    3.0
    >>> round(10.0/3, 0)
    3.0

In Python 3 rounding of halfway cases are now always towards the nearest even. This is standard practice, as it will make a set of evenly distributed roundings average out.

When called without the second parameter, which determines the number of decimals, round() will in Python 3 return an integer. If you pass in a parameter to set the number of decimals to round to, the returned value will be of the same type as the unrounded value. This is true even if you pass in zero.::

    >>> round(1.5)
    2
    >>> round(2.5)
    2
    >>> round(10.0/3, 0)
    3.0

If you need the Python 2 behavior, you can use the following method::

    >>> import math
    >>> def my_round(x, d=0):
    ...     p = 10 ** d
    ...     return float(math.floor((x * p) + math.copysign(0.5, x)))/p
    
    >>> my_round(1.5)
    2.0
    >>> my_round(2.5)
    3.0
    >>> my_round(10.0/3, 0)
    3.0

Slice operator methods
-------------------------------

In Python 1 you used __getslice__ and __setslice__ to support slice methods like foo[3:7] on your object. These were deprecated in Python 2.0 but still supported. Python 3 removes the support for the slice methods, so you need to instead extend __getitem__, __setitem__ and __delitem__ with slice object support.

Sorting
--------

Use the sorted function as much as possible instead of the .sort() method so as to use the key parameter. If you still want to use sort(), use the key parameter (not cmp)::

    >>> def keyfunction(item):
    ...     """Key for comparison that ignores the first letter"""
    ...     return item[1:]
    >>> names = ['Adam', 'Donald', 'John']
    >>> names.sort(key=keyfunction)
    >>> names
    ['Adam', 'John', 'Donald']

StandardError
-------------------

Python 2 has an exception class called StandardError that has been removed in Python 3. Use Exception instead.

String types
------------------

Python 2 had two string types; str and unicode. 
Python 3 has only one; str, but instead it also has a bytes type made to handle binary data. 


Bytes, strings and unicode
-------------------------------

- strings are always unicode in Python 3
- since strings are now always Unicode, we need another type for binary data. Python 3 has two binary types:
    - bytes : similar to string type but is a strint of integers instead of characters
    - bytearrays: like a list but that hold integers between 0 and 255. Is mutable and used to manipulate binary data.

Bytes literals
----------------
Nice and complete explanation here: http://python3porting.com/problems.html#binary-section




List of common modules
========================

This is absolutely not exhaustive but based on my own packages and usage!

============== ==========================
Module name     Comment
============== ==========================
dl              Supplanted by ctypes
exception       See above
htmllib         Supplanted html.parser
mimetools       Supplanted by email
popen2          Supplanted by subprocess
sha             Supplanted by hashlib
stat            Supplanted by os.stat()
thread          Supplanted by threading
============== ==========================

itertools
============

In Python 2, the itertools module defines variants of the global zip(), map(), and filter() functions that returned iterators instead of lists. In Python 3, those global functions return iterators, so those functions in the itertools module have been removed.

========================== =================
Python 2                    Python 3
========================== =================
itertools.izip(a, b)        zip(a, b)
itertools.imap(a, b)        map(a, b)
itertools.ifilter(a, b)     filter(a, b)
========================== =================


urllib, urlparse, urllib2
============================

The three modules urllib, urllib2 and urlparse has been reorganized into three new modules, urllib.request, urllib.parse and urllib.error. 

In brief:

======================================  ===================================================
Python2                                 Python3
======================================  ===================================================
import urllib                           import urllib.request, urllib.parse, urllib.error
import urllib2                          import urllib.request, urllib.error
import urlparse                         import urllib.parse
import robotparser                      import urllib.robotparser
from urllib import FancyURLopener       from urllib.request import FancyURLopener
from urllib import urlencode            from urllib.parse import urlencode
from urllib2 import Request             from urllib.request import Request
from urllib2 import HTTPError           from urllib.error import HTTPError
======================================  ===================================================

More details:

==================================  =========================
Python 2 name                       Moved to
==================================  =========================
urllib._urlopener                       urllib.request
urllib.ContentTooShortError             urllib.error
urllib.FancyURLOpener                   urllib.request
urllib.pathname2url                     urllib.request
urllib.quote                            urllib.parse
urllib.quote_plus                       urllib.parse
urllib.splitattr                        urllib.parse
urllib.splithost                        urllib.parse
urllib.splitnport                       urllib.parse
urllib.splitpasswd                      urllib.parse
urllib.splitport                        urllib.parse
urllib.splitquery                       urllib.parse
urllib.splittag                         urllib.parse
urllib.splittype                        urllib.parse
urllib.splituser                        urllib.parse
urllib.splitvalue                       urllib.parse
urllib.unquote                          urllib.parse
urllib.unquote_plus                     urllib.parse
urllib.urlcleanup                       urllib.request
urllib.urlencode                        urllib.parse
urllib.urlopen                          urllib.request
urllib.URLOpener                        urllib.request
urllib.urlretrieve                      urllib.request
urllib2.AbstractBasicAuthHandler        urllib.request
urllib2.AbstractDigestAuthHandler       urllib.request
urllib2.BaseHandler                     urllib.request
urllib2.build_opener                    urllib.request
urllib2.CacheFTPHandler                 urllib.request
urllib2.FileHandler                     urllib.request
urllib2.FTPHandler                      urllib.request
urllib2.HTTP*                           urllib.request
urllib2.install_opener                  urllib.request
urllib2.OpenerDirector                  urllib.request
urllib2.ProxyBasicAuthHandler           urllib.request
urllib2.ProxyDigestAuthHandler          urllib.request
urllib2.ProxyHandler                    urllib.request
urllib2.Request                         urllib.request
urllib2.UnknownHandler                  urllib.request
urllib2.URLError                        urllib.request
urllib2.urlopen                         urllib.request
urlparse.parse_qs                       urllib.parse
urlparse.parse_qsl                      urllib.parse
urlparse.urldefrag                      urllib.parse
urlparse.urljoin                        urllib.parse
urlparse.urlparse                       urllib.parse
urlparse.urlsplit                       urllib.parse
urlparse.urlunparse                     urllib.parse
urlparse.urlunsplit                     urllib.parse
==================================  =========================
