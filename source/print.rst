
.. index:: 
   single: print 

.. _print_section:

Print function
#################

.. seealso:: :ref:`string_section`

Quick Example
==================

In order to print the Hello world string, use the :func:`print` function as follows::

    >>> print("Hello")
    Hello

is the correct way to print a string. Note; however, that is Python 2.X, you could also write::

    >>> print "Hello"
    Hello

print blank line(s)
=====================

Let us print 5 blank lines. You can naively type::


    print(5 * "\n")

or::

    print("\n\n\n\n\n")

or even better::

    print(5 * "\n")

Print an object without a trailing newline
=============================================

By default, the print function add a trailing line. To prevent this behavious, add a comma after the statement::

    >>> x, y = 1, 2
    >>> print(x),; print(y)
    1 2

you could use::

    print x,y,

Formatted strings
=======================

The special operator % lets you create formatted output. It takes two operands: a formatted string and a value. The value can be a single value, a tuple of values or a dictionary of values. For example::

    print("pi=%s" % "3.14159")

The formatted string has a **conversion specifiers** that also uses the special characters **%s**.  This conversion specifier tells Python how to convert the value. Here %s means convert the value to a string. In fact, you could even type::

    print("pi=%s" % 3.14159)

because the right operand (given the conversion specifiers) should be converted with :func:`str`.

To be more generic, you could include the value within a tuple::

    print("pi=%s" % (3.14159))

and print 2 values:: 

    print("%s=%s" % ("pi", 3.14159))

The conversion specifiers can also convert values into float, integers and so on. See :ref:`conversion_types`. The conversion specifiers can be tuned and the following sections will show you how. First, let us have a look at special characters.


Special characters
===================

To escape the sign *%*, just double it::

    >>> print "This is a percent sign: %%"
    This is a percent sign: %

Other special characters similar to some other languages are summarized in the following table:


=========== ======== ==============================================
character   Decimal  Description
=========== ======== ==============================================
\\                   statement continues on next line
\\\         92       backslash
\\'         39       Single quote
\\"         34       Double quote
\\a         7        Bell
\\b         8        Backspace
\\f                  Formfeed
\\n         10       newline
\\r         13       carriage return
\\t         9        tabulation
\\v         11       vertical tabulation
\\0 \\000            null value
\\ooo                octal value o in (0..7)
\\xhh                hexadecimal value (0..9, a..f; A..F)
\\uxxxx              Unicode character value
=========== ======== ==============================================



More about conversion specifiers
================================

The general syntax for a conversion specifier is::

    %[(key)][flags][width][.prec]type

Let us see each option in details. Let us start with the meaning of **type**.

.. _conversion_types:

Conversion types
-------------------

We have already seen one type: the string type %s. The following table summarizes all the available types:

=============== =======================================================
character       Description
=============== =======================================================
c               Converts to a single character
d,i             Converts to a signed decimal integer or long integer
u               Converts to an unsigned decimal integer
e,E             Converts to a floating point in exponential notation
f               Converts to a floating point in fixed-decimal notation
g               Converts to the value shorter of %f and %e
G               Converts to the value shorter of %f and %E
o               Converts to an unsigned integer in octal
r               string generated with repr()
s               Converts to a string using the str() function
x,X             Converts to an unsigned integer in hexadecimal
=============== =======================================================




Formatting string with a dictionary
---------------------------------------

Let us now look at the **key** option. This key refer to the keys used in dictionaries.
It works as follows::

    >>> print("%(key1)s and %(key2)%" % {'key1':1, 'key2':2})
    "1 and 2"

Flags
--------

The second type of options are the flags:

=========== ===================================================  ===================== ============
character   Description                                          example                rendering
=========== ===================================================  ===================== ============
0           pad **numbers** with leading weros                   "(%04d)" % 2            0002
\-           left align the results (default is right)
space       add a space before a positive number or string
\+           Always begin a number with a sign (+or-)
#           display numbers in alternate form.
=========== ===================================================  ===================== ============

The *width* option
----------------------

The *width* option is a positive integer specifying the minimum field width. If the converted value is shorter than *width*, spaces are added on left or right (depending on *flags*)::


    >>> print("(%10s)" %  "example")
    (   example)
    >>> print("(%-10s)" %  "example")
    (example   )

Specific number of digits with the *prec* option
-------------------------------------------------

*prec* is a dot (.) followed by a positive integer specifying the precision. Note that use the %f conversion specifier here::

    >>> print("%.2f" %  2.012)
    2.01




Dynamic formatter
------------------

Sometimes, you want to format a string but you do not know its size. In such case, you can use a dynamic formatter using the * character as follows::

     >>> print  '%*s : %*s' % (20, "Python", 20, "Very Good")
                  Python :            Very Good






The format string method in details
========================================

The replacement field {}
------------------------------

Let us consider this example::

    >>> x = "example"
    >>> "{0} {1}".format("The", x)
    "The example"

The {} is a replacement field identified by braces and a name (or index). If an index is provided, it is the index of the list of argument provided in the **format** call. In the example above, we could have written (with the same output)::

    >>> "{1} {0}".format(x, "The")
    "The example"

With name, we add robusteness::

    >>> "{first} {second}".format(first="The", second=x)
    "The example"

We can combine name and indices::    

    >>> "{0} {second} {1}".format("The", x, second="second")
    'The second example'


Note that *index* argument should be provided before the *name* argument. This does not work::

    >>> "{0} {second} {2}".format("The", second="second", x)


Another neat way is to provide a dictionary::

    >>> d = {"first":"The", "second": x}
    >>> "{0[first]} {0[second]} {1}".format(d, "with dictionary")
    "The example with dictionary"

You can even use attribute from class, import::

    >>> import math
    >>> "{0.pi}".format(math)
    3.14159265359


So, you can use positional arguments combined with variable, list, dictionary, attribute)::

    >>> class A():x=1
    >>> a = A()
    >>> "{0} {1[2]} {2[test]} {3.x}".format("This", ["a", "or", "is"], {"test":"another"}, a)
    "This is another example"

The replacement field can be further altered using these syntax::

    {fieldname}
    {fieldname!conversion}
    {fieldname:format-spec}
    {fieldname!conversion:format-spec}

conversion
--------------------

Let us first explain the difference between the string form and the representational form. Consider the **Decimal** class from the :mod:`decimal` module. When you type the name of a variable/instance, it prints a representational form of the instance::

    >>> decimal.Decimal('3.40')
    Decimal('3.40')

The print command actually prints something different::

    >>> print(decimal.Decimal('3.40'))
    3.40

Note the absence of quotes. Here, the print behaviour is defined by the special method **__str__**. THe representational form is convenient if you want to recreate the instance. The string form is for human-friendly form.

Now, the format convertion can allow you to choose one or the other::


    >>> "{0!s}".format(decimal.Decimal('3.40'))
    '3.40'
    "{0!r}".format(decimal.Decimal('3.40'))
    "Decimal('3.40')"



Format convertion have several types:

======= ========================================
======= ========================================
    s   force string form
    r   force representational form
    a   force representational form using ASCII
======= ========================================


format specifications
-------------------------------


The format specifications is provided using the *:* character::

    >>> "{0:10}".format("test")
    'test      '


The full syntax is as follows:


========== ========== ======= ============== ============= ====== ========= ===============
fill       align      sign    #              0             width  precision type
========== ========== ======= ============== ============= ====== ========= ===============
any        < left     +       a prefix       0-pad numbers                  all C types
character  > right    -       for int                                       e.g., b,c,d,n,
           ^ center   space   0b, 0o or 0x                                  X, e, E
           = padding
========== ========== ======= ============== ============= ====== ========= ===============


::

    >>> "{0:0x}".format(111)
    1101111

    >>> "{0:08}".format(111)
    '00000111'


    >>> "{0:*<8}".format(1234) # fill with * characters on the right to have a string of length 8
    '1234****



Final example
====================


This example uses the :mod:`sys`, and :mod:`unicodedata` modules.

::

    import sys, unicodedata
    print("Decimal hex   chr   {0:^40}".format("none"))
    print("------- ----- ----- {0:-<40}".format(""))
    code = ord(" ")
    end = sys.maxunicode
    while code<end:
        c = unicode(unichr(code))
        name = unicodedata.name(c, "***unknown***")
        if word is None or word in name.lower():
            print("{0:7} {0:5x} {0:^3c} {1}".format(code, name.title()))
            
        code += 1


::

    Decimal hex   chr                     none                  
    ------- ----- ----- ----------------------------------------
    9250    2422  "     Blank Symbol
    10240   2800        Braille Pattern Blank

