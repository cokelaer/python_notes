Notes on tricky issues in Python
================================

Declaration of an array of instance
-----------------------------------

Given a class **Person** with no parameters, the correct way to declare  
an array of Person instances is::

    [Person() for x in range(3)]


Do not use the following syntax::

    3 * [Person()]

Although this syntax is correct, it provides 3 identical instances (that refer to the same instance), which is not what we want. 


Passing arguments
-----------------


By default, passing arguments in Python is made by value for simple types and by references for objects. You can not pass an object by value (in C++ you can decide to use or not the & symbol). 

The following example illustrate the passing argument by value case:

.. doctest::

    >>> def swap(a, b):
    ...    (b, a) = (a, b)
    >>> a = 1
    >>> b = 2
    >>> swap(a, b)
    >>> a
    1

And this example illustrates the passing argument by reference case:

.. doctest::

    >>> # First, we create a function that change the attribute 'data'
    >>> def init_object(o):
    ...     o.data = 0.
    >>> # Second, we create an empty class that will be populated later
    >>> class P(): pass
    >>> # Let us create an instance and set the attribute data to 100.
    >>> o = P()
    >>> o.data = 100.
    >>> # let us call the function (by reference)
    >>> init_object(o)
    >>> o.data
    0.0



The underscore character
----------------------------

* As a convention, the underscore character can be used in front of a variable to indicate it is a private variable, which should not be used then.
* If you use the double underscore prefix such as __arg2, Python uses name-mangling to make it a private variable. However, you can still access to it if you want, so this is not a pure private data.
* Finally, the underscore character can also be used to **hide** a variable. For instance in a loop statement, the variable to loop over can simply be called **_**, which is a valid pytho variable::

    for _ in (0,1,2):
        # do something
        print(_)

* Note that a variable called **_** is often used with the gettext.gettext function.





