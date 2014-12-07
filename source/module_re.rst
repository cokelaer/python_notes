.. testsetup:: *

    import re

The regular expression module
###############################

The :mod:`re` module implements regular expression searches.
There are entire books about regular expressions and we will not cover all the possibilities but will present only a few examples to give an idea of what can be achieved with regular expressions.

Examples here below are inspired or taken from the references (e.g. dive into python).

Quick start
=============

You can use this module to search for strings using wildcards and complex patterns. Here is a first set of examples to illustrate the difference between the :func:`re.match` and :func:`re.search` functions:

.. doctest::

    >>> s = ['airplane', 'base', 'ALLIGATOR', 'Broad' ]
    >>> filter((lambda x: re.match(r'A', x)),s)
    ['ALLIGATOR']
    >>> filter((lambda x: re.match(r'L', x)),s)
    []
    >>> filter((lambda x: re.search(r'L', x)),s)
    ['ALLIGATOR']
    >>> filter((lambda x: re.search(r'^L', x)),s) 
    []

The :func:`re.match` function searches for a pattern at the start of the string, which explains that with the pattern `L` nothing is found. Conversely, the :func:`re.search` method searches for the pattern everywhere, except if the sign ^ is used, which indicates to start at the beginning of the string.

Here is another set of examples to illustrate the usage of the dot character:

.. doctest::

    >>> s = ('xxx', 'abcxxxabc', 'xyx', 'abc', 'x.x', 'axa', 'axxxxa', 'axxya')
    >>> # let us search for all strings with at least 2 consecutive 'x'
    >>> filter((lambda x: re.search(r'xx', x)),s) 
    ('xxx', 'abcxxxabc', 'axxxxa', 'axxya')
    >>> # now, we want 2 consecutives 'x'
    >>> filter((lambda x: re.search(r'xx', x)),s) 
    ('xxx', 'abcxxxabc', 'axxxxa', 'axxya') 
    >>> # or 2 x separated by a character
    >>> filter((lambda x: re.search(r'x.x', x)),s) 
    ('xxx', 'abcxxxabc', 'xyx', 'x.x', 'axxxxa')

The dot is a special character, so to look for it, you need to escape it::

    >>> filter((lambda x: re.search(r'x\.x', x)),s) 
    ('x.x', )

finally, for this quick start, let us show the difference between the plus and asterisk characters.

The **asterisk** matches **zero or more occurences** of a character, so 'x*x' matches 'axa'::

    >>> filter((lambda x: re.search(r'x*x', x)),s) 
    ('xxx', 'abcxxxabc', 'xyx', 'x.x', 'axa', 'axxxxa', 'axxya')

Instead, you may want to use the **plus** sign that matches **one or more occurences**::

    >>> filter((lambda x: re.search(r'x+x', x)),s)
    ('xxx', 'abcxxxabc', 'axxxxa', 'axxya')


Matching at the End of a String
===============================

A first naive approach is to use the :meth:`replace` method of a string:

.. doctest::

    >>> s = '100 BROAD ROAD'
    >>> s.replace('ROAD', 'RD.')
    '100 BRD. RD.'

but as you can see, all instances of **ROAD** are replaced, which is not what we want. We could use a trick to search for ** ROAD** (note the space before ROAD). 

.. doctest::

    >>> s = '100 BROAD ROAD'
    >>> s.replace(' ROAD', 'RD.')
    '100 BROAD RD.'

Another way is to split the string and replace the **ROAD** string where it is appropriate but again this is not an ideal solution.

.. doctest::

    >>> s = '100 BROAD ROAD'
    >>> s[:-4] + s[-4:].replace('ROAD', 'RD.')
    '100 BROAD RD.'

Using the regular expression, we can matche the **ROAD** when it occurs at the end of the string. Here the $ sign means end of string. The caret sign (^) means beginning of the string.  

.. doctest::

    >>> import re
    >>> s = '100 BROAD ROAD'
    >>> re.sub('ROAD$', 'RD.', s)
    '100 NORTH BROAD RD.'

This matches the ROAD at the end of the string s, but does not match the ROAD that's part of the word BROAD, because it is in the middle of s.


.. index:: raw string operator

Matching Whole Words
====================

To express a whole word, you use ``\b``, which  means "a word boundary must occur right here". In Python, this is complicated by the fact that the ``\``  character in a string must itself be escaped. It is one reason why regular expressions are easier in Perl than in Python. 

.. doctest::

    >>> s = '100 BROAD'
    >>> re.sub('ROAD$', 'RD.', s)
    '100 BRD.'
    >>> re.sub('\\bROAD$', 'RD.', s)
    '100 BROAD'

To work around the backslash plague, you can use what is called a raw string, by prefixing the string with the letter r. This tells Python that nothing in this string should be escaped; 

.. doctest:: 

    >>> re.sub(r'\bROAD$', 'RD.', s)
    '100 BROAD'
    >>> s = '100 BROAD ROAD APT. 3'
    >>> re.sub(r'\bROAD$', 'RD.', s)
    '100 BROAD ROAD APT. 3'
    >>> re.sub(r'\bROAD\b', 'RD.', s)
    '100 BROAD RD. APT. 3'


Here are more examples:    


.. doctest::

    >>> import re
    >>> pattern = r'^M?M?M?$'        # match either M, MM or MMM as a whole word
    >>> re.search(pattern, 'M')     # returns True #doctest: +SKIP 
    >>> pattern = r'^M?M?M?(X|C|D)$'
    >>> re.search(pattern, 'MMD')     # returns True #doctest: +SKIP 
    >>> re.search(pattern, 'MMDX')     # returns False because D is not the fina l character #doctest: +SKIP 
    

{n,m} notation for pattern 
==========================

.. doctest:: 

    >>> pattern = '^M{0,3}$'
    >>> re.search(pattern, 'MM') #doctest: +SKIP


Regular Expressions with Inline Comments
========================================

It could be handy to store the pattern with comments within a triple quoted string. 
This example checks roman numbers validity:

.. doctest::
    :options: +SKIP

    >>> pattern = """
    ^                     #  beginning of string
    M{0,4}                #  thousands - 0 to 4 M's
    (CM|CD|D?C{0,3})      #  hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
                          #             or 500-800 (D, followed by 0 to 3 C's)
    (XC|XL|L?X{0,3})      #  tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
                          #          or 50-80 (L, followed by 0 to 3 X's)
    (IX|IV|V?I{0,3})      #  ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
                          #          or 5-8 (V, followed by 0 to 3 I's)
    $                     #  end of string
    """
    >>> re.search(pattern,   'M', re.VERBOSE)
    <_sre.SRE_Match object   at 0x008EEB48>
    >>> re.search(pattern,   'MCMLXXXIX', re.VERBOSE)
    <_sre.SRE_Match object   at 0x008EEB48>
    >>> re.search(pattern,   'MMMMDCCCLXXXVIII', re.VERBOSE)

Others
======

To get access to the groups that the regular expression parser remembered along the way, use the groups() method on the object that the search function returns.




Summary
=======
* ^ matches the beginning of a string.
* $ matches the end of a string.
* ``\b`` matches a word boundary.
* ``\d`` matches any numeric digit.
* ``\D`` matches any non-numeric character.
* x? matches an optional x character (in other words, it matches an x zero or one times).
* x* matches x zero or more times.
* x+ matches x one or more times.
* x{n,m} matches an x character at least n times, but not more than m times.
* (a|b|c) matches either a or b or c.
* (x) in general is a remembered group. You can get the value of what matched by using the groups() method of the object returned by re.search.

* ``\D+`` matches any character except a numeric digit, and + means "1 or more". 
* ``\D*`` matches any character except a numeric digit, and + means "0 or more".

wildcards
===========

========= ================================================ =========================================================
Wildcard   Matches                                          Example
========= ================================================ =========================================================
`*`        any characters                                  `*.txt`   matches all files with the txt extension
?          any one character                               `???`     matches files with 3 characters long
[]         any character listed in the  brackets           `[ABC]*`  matches files starting with A,B or C
[..]       any character in the range listed in brackets   `[A..Z]*` matches files starting with capital letters
[!]        any character listed in the  brackets           `[!ABC]*` matches files that do not start with A,B or C
========= ================================================ =========================================================



References
=============

#. [Dive]_, page 80
#. [Norton]_ Chap 10
