The string module 
##################################

The :mod:`string` module provides additional tools to manipulate strings. Some methods available in the standard data tstructure are not available in the string module (e.g., isalpha).

Quick start
=============

::

    >>> string.digits
    '0123456789'

    >>> string.punctuation
    '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    >>> string.lowercase
    'abcdefghijklmnopqrstuvwxyz'
    >>> string.letters
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    >>> string.uppercase
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

The following 3 function are equivalent to the previous 3 functions: string.ascii_letters, string.ascii_lowercase, string.ascii_uppercase       

::

    >>> string.expandtabs("a a\t",4)
    'a a    '

    >>> string.whitespace
    '\t\n\x0b\x0c\r '

    >>> string.octdigits
    '01234567'

    >>> string.hexdigits
    '0123456789abcdefABCDEF'

:func:`string.printable` function is the concatenation of letterm digits and punctuation.

Capitalise each word of the sentence::

    >>> string.capwords("this is a test")
    'This Is A Test'




string.splitfields equivalent to the split method of a string
string.joinfields equivalent to the join method of a string

There are deprecated functions atof, atoi, atol
::

    >>> string.atof("2")
    2.0

equivalent to ::

    >> float("2")

You also have the atoi (cast to integer) and atol (cast to long) 


A function of interest is string.maketrans. Can be used together with the translate method of the string data structure.

Return a translation table suitable for passing to translate(), that will map each character in from into the character at the same position in to; from and to must have the same length.

::

    >>> t = string.maketrans("acgt", "tgca")
    >>> "acgttgca".translate(t)
    'tgcaacgt'


The Formatter class in the string module allows you to create and customize your own string formatting behaviors using the same implementation as the built-in format() method.

string.Formatter   
~~~~~~~~~~~~~~~~~~~

Templates provide simpler string substitutions as described in PEP 292. Instead of the normal %-based substitutions, Templates support $-based substitutions, using the following rules:


string.Template                   
~~~~~~~~~~~~~~~~~~~

::

    >>> from string import Template
    >>> s = Template('$who likes $what')
    >>> s.substitute(who='tim', what='kung pao')
    'tim likes kung pao'
    >>> d = dict(who='tim')
    >>> Template('Give $who $100').substitute(d)
    Traceback (most recent call last):
    ...
    ValueError: Invalid placeholder in string: line 1, col 11
    >>> Template('$who likes $what').substitute(d)
    Traceback (most recent call last):
    ...
    KeyError: 'what'
    >>> Template('$who likes $what').safe_substitute(d)
    'tim likes $what'







