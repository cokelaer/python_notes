.. contents::



.. index:: strings, formatter


.. _string_section:

Strings
#########

.. seealso:: :ref:`print_section`


In short, strings are immutable sequence of characters. There are a lot of methods to ease manipulation and creation of strings as shown here below.

Creating a string (and special characters)
=============================================

Single and double quotes are special characters. There are used to defined strings. There are actually 3 ways to define a string using either single, double or triple quotes::

    text = 'The surface of the circle is 2 pi R = '
    text = "The surface of the circle is 2 pi R = "
    text = '''The surface of the circle is 2 pi R = '''

In fact the latest is generally written using triple double quotes::

    text = """The surface of the circle is 2 pi R = """

Strings in double quotes work exactly the same as in single quotes but allow to insert single quote character inside them. 

The interest of the triple quotes (''' or """) is that you can specify multi-line strings. Moreover, single quotes and double quotes can be used freely within the triple quotes::

     text = """ a string with special character " and ' inside """

The " and ' characters are part of the Python language; they are special characters. To insert them in a string, you have to escape them (i.e., with a \\ chracter in front of them to indicate the special nature of the character). For instance::

     text = " a string with escaped special character \", \' inside "

There are a few other special characters that must be escaped to be included in a string. See :ref:`print` for more information.

To include unicode, you must precede the string with the **u** character::

    >>> u"\u0041"
    A

.. note:: unicode is a single character set used to represent 65536 different characters. 
.. seealso:: See :ref:`encode` for more information about unicode.

Similarly, you may see strings preceded by the **r** character to indicate that the string has to be interpreted as it is without interpreting the special character **\\**. This is useful for docstrings that contain latex code for instance::

    r" \textbf{this is bold text in LaTeX} "


.. seealso:: See :ref:`print` for more information about string format and printing.


Strings are immutable
======================

You can access to any character using slicing::

    text[0]
    text[-1]
    text[0:]

However, you cannot change any character::

    text[0] = 'a' #this is incorrect.


Note that when slicing, you get a new string except if the indices match the
start and end of the original string, in which case the original string is
returned.


Formatter
============

In Python, the % sign lets you produce formatted output. A quick example will illustrate how to print a formatted string::

   >>> print("%s" % "some text")
   "some text"

The syntax is simply::

    string % values

If you have more than one value, they should be placed within brackets::

    >>> print("%s %s" % ("a", "b"))

The string contains characters and *conversion specifiers* (here %s)

To escape the sign %, just double it::

    >>> print "This is a percent sign: %%"
    This is a percent sign: %

There are different ways of formatting a string with arguments. The one based on a string method called :meth:`~str.format` is more and more common::

    >>> "{a}!={b}".format(a=2, b=1)
    2!=1


.. seealso:: :ref:`print_section`


Operators
=================
 

The mathematical operators ``+`` and ``*`` can be used to create new strings::

    t = 'This is a test'
    t2 = t+t
    t3 = t*3

and comparison operators ``>``, ``>=``, ``==``,  ``<=``, ``<`` and ``!=`` can be used to compare strings.



Methods
=========

The string methods are numerous, however, many of them are similar (as you will see in this page).

    
.. index:: isdigit, isalpha, isupper, islower, isspace, istitle, isalnum

Methods to query information
-----------------------------
There are a few methods to check the type of alpha numeric characters present in a string: :meth:`~str.isdigit`, :meth:`~str.isalpha`, :meth:`~str.islower`, :meth:`~str.isupper`, :meth:`~str.istitle`, :meth:`~str.isspace`, :meth:`str.isalnum`:

.. doctest::

    >>> "44".isdigit()  # is the string made of digits only ?
    True
    >>> "44".isalpha()  # is the string made of alphabetic characters only ?
    False
    >>> "44".isalnum()  # is the string made of alphabetic characters or digits only ?
    True
    >>> "Aa".isupper()  # is it made of upper cases only ?
    False
    >>> "aa".islower()  # or lower cases only ?
    True
    >>> "Aa".istitle()  # does the string start with a capital letter ?
    True
    >>> text = "There are spaces but not only"
    >>> text.isspace() # is the string made of spaces only ?
    False

You can count the occurence of a character with :meth:`~str.count` or get the length of a string with :func:`len`:

.. doctest::

    >>> mystr = "This is a string"
    >>> mystr.count('i')
    3
    >>> len(mystr)
    16

.. index:: title, capitalize, lower, upper , swapcase

Methods that return a modified version of the string
------------------------------------------------------

The following methods return modified copy of the original string, which is immutable.

First, you can modify the cases using :meth:`~str.title`, :meth:`~str.capitalize`, :meth:`~str.lower`, :meth:`~str.upper` and :meth:`~str.swapcase`:

.. doctest::

    >>> mystr = "this is a dummy string"
    >>> mystr.title()       # return a titlecase version of the string
    'This Is A Dummy String'
    >>> mystr.capitalize()  # return a string with first letter capitalised only.
    'This is a dummy string'
    >>> mystr.upper()       # return a capitalised version of the string
    'THIS IS A DUMMY STRING'
    >>> mystr.lower()       # return a copy of the string converted to lower case
    'this is a dummy string'
    >>> mystr.swapcase()    # replace lower case by upper case and vice versa
    'THIS IS A DUMMY STRING'

.. index:: center, just, ljust, rjust

Second, you can add trailing characters with :meth:`~str.center` and :meth:`~str.just` methods:

.. doctest::

    >>> mystr = "this is a dummy string"
    >>> mystr.center(40)              # center the string in a string of length 40
    '         this is a dummy string         '
    >>> mystr.ljust(30)               # justify the string to the left (width of 20)
    'this is a dummy string        '
    >>> mystr.rjust(30, '-')          # justify the string to the right (width of 20)
    '--------this is a dummy string'

.. index:: zfill, strip, rstrip, lstrip, expantabs

There is also a :meth:`~str.zfill` methods that adds zero to the left, which is equivalent to ``.rjust(width, '0')``::

    >>> mystr.zfill(30)
    '00000000this is a dummy string'

or remove trailing spaces with the :meth:`~str.strip` methods:

.. doctest::

    >>> mystr = "  string with left and right spaces   "
    >>> mystr.strip()
    'string with left and right spaces'
    >>> mystr.rstrip()
    '  string with left and right spaces'
    >>> mystr.lstrip()
    'string with left and right spaces   '

or expand tabs with :meth:`~str.expandtabs`::

    >>> 'this is a \t tab'.expandtabs()
    'this is a     tab'

.. index:: translate, partition, rpartition

You can remove some specific characters with :meth:`~str.translate` or replace words with :meth:`~str.replace`::

    >>> mystr = "this is a dummy string"
    >>> mystr.replace('dummy', 'great', 1)  # the 1 means replace only once
    'this is a great string'
    >>> mystr.translate(None, 'aeiou')
    ths s dmmy strng

Finally, you can separate a string with respect to a single separator with :meth:`~str.partition`::

    >>> mystr = "this is a dummy string"
    >>> t.partition('is')
    ('th', 'is', ' is a line')
    >>> t.rpartition('is')
    ('this ', 'is', ' a line')

.. index:: endswith, startswith, find, index, rfind, rindex, rfind

Methods to find position of substrings
-------------------------------------------
The are methods such as :meth:`~str.endswith`, :meth:`~str.startswith`, :meth:`~str.find` and :meth:`~str.index` that allow to search for substrings in a string.

.. doctest::

    >>> mystr = "This is a dummy string"
    >>> mystr.endswith('ing')       # may provide optional start and end indices
    True
    >>> mystr.startswith('This')    # may provide start and end indices
    True
    >>> mystr.find('is')            # returns start index of 'is' first occurence
    2
    >>> mystr.find('is', 4)         # starting at index 4, returns start index of 'is' first occurence
    5
    >>> mystr.rfind('is')           # returns start index of 'is' last occurence
    5
    >>> mystr.index('is')           # like find but raises error when substring is not found
    2
    >>> mystr.rindex('is')          # like rfind but raises error when substring is not found
    5

.. index:: split, join

Methods to build or decompose a string
------------------------------------------

A useful function is the :meth:`~str.split` methods that splits a string according to 
a character. The inverse function exist and is called :meth:`~str.join`.

.. doctest::

    >>> message = ' '.join(['this' ,'is', 'a', 'useful', 'method'])
    >>> message
    'this is a useful method'
    >>> message.split(' ')
    ['this', 'is', 'a', 'useful', 'method']

The :meth:`~str.split` function can be applied to a limited number of times if needed. However, it starts from the left. If you want to start from the right, use :meth:`~str.rsplit` instead::

    >>> message = ' '.join(['this' ,'is', 'a', 'useful', 'method'])
    >>> message.rsplit(' ', 2)
    ['this is a', 'useful', 'method']


If a string is multi-lines, you can split it with :meth:`~str.splitlines`:

.. doctest::

    >>> 'this is an example\n of\ndummy sentences'.splitlines()
    ['this is an example', ' of', 'dummy sentences']

you can keep the endline character by giving True as an optional argument.

Finally, note that :meth:`~str.split` removes the splitter::

    >>> "this is an exemple".split(" is ")
    ['this', 'an exemple']

If you want to keep the splitter as well, use :meth:`~str.partition` ::

    >>> "this is an exemple".partition(" is ")
    ('this', ' is ', 'an exemple')





.. index:: decode, encode

.. _encode:

Encoding/Decoding/Unicode
------------------------------

We've seen how to create a unicode by adding the letter **u** in front of a string::

    s = u"\u0041"

The function :func:`unicode` converts a standard string to unicode string using the encoding specified as an argument (default is the default string encoding)::

    s = unicode("text", "ascii")

In order to figure out the default encoding, type::

    >>> import sys
    >>> sys.getdefaultencoding()
    'ascii'

Here are some encodings::

    ascii, utf-8, iso-8859-1, latin-1, utf-16, unicode-escape.

The unicode function takes also a third argument set to: 'strict', 'ignore' or 'replace'.

Let us take another example with accents::


    >>> # Let us start wil a special character.
    >>> text = u"π"
    >>> # to obtain its code (in utf-8), let us use the encode function
    >>> encoded = text.encode("utf-8")
    >>> decoded = text.decode("utf-8")



.. todo:: examples



