.. _namespace_scope:

Namespace and scoping rules
##############################

Only 3 namespaces are visible to the developer: local, global, built-in. 

You can obtain the loca namespace with::

    locals()

and the global one with::

    globals()

There are 2 dictionaries so you can get the key/value pairs.


.. todo:: this section will present namespace and scopes

local namespace
 parameter names
 local variable names

global namespace (module-level)
 function names
 class names
 import modules names
 variable names
 global variables names in functions


built-in namespace (predefined names). built-in function names: len, str
built-in exception names (TypeError)



Let us consider a function with only one local variable::

    >>> def A(b):
    ...    x=1
    ...    print locals()
    >>> A()
    {'x': 1, 'b': 1}


The :func:`vars` return a dictionary corresponding to the local namespace of an object (e.g., a module)::

    import math
    vars(math)


Without an object, :func:`vars` returns the same as :func:`locals`.


To get the built-in namespace, type ::

    dir(__builtin__)

to obtain a sorted list of names in the built-in namespace and ::

    vars(__builtin__)

to obtain the dictionary correspondinf to the built-in namespace.



See :ref:`globals` for an example using a function.


nested functions
=======================

Since python 2.1, nested scopes are available, which means that python searches for variables in the function's namespace, then in the parent's function namespace, and finally in the module's namespace

::

    c = 1
    def func1(a, b):

        def inner_func(x):
            return x*x*x + c

        return inner_func(a) + inner_func(b)

is valid code, c=1 will be used within the inner function.

