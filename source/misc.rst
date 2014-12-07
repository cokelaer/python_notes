
conditional assignements
===========================

::

    x = 3 if (y == 1) else 2

It does exactly what it sounds like: "assign 3 to x if y is 1, otherwise assign 2 to x". Note that the parens are not necessary, but I like them for readability. You can also chain it if you have something more complicated::

    x = 3 if (y == 1) else 2 if (y == -1) else 1

Though at a certain point, it goes a little too far.

Note that you can use if ... else in any expression. For example::

    (func1 if y == 1 else func2)(arg1, arg2) 

Here func1 will be called if y is 1 and func2, otherwise. In both cases the corresponding function will be called with arguments arg1 and arg2.

Analogously, the following is also valid::

    x = (class1 if y == 1 else class2)(arg1, arg2)


where class1 and class2 are two classes.
