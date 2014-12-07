Decorators
=============

Quickstart
-----------

The following code is made of a simple division function that takes an input argument, which may be zero. In such
case, the function raise a ZeroDivision exception. The decorator (check_validity) goal is to return False and not to 
raise any excption. 

::

    def check_validity(f):
        def wrap(*args):
            if args[0] == 0:
                return False
            return f(*args)
        return wrap

    @my_decorator
    def division(n):
        return 100./n


Decorator without argument for a function with arguments and optional arguments
------------------------------------------------------------------------------------

This is exaclty the same principle as in the quick start example. Here, we added the optional arguments l=10 and therefore kargs in the decorator.

.. automodule:: decorators

.. literalinclude:: decorators.py







