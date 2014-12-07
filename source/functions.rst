.. _functions:


Functions
###########

.. index:: function, return

Introduction
==============


.. index:: def, global, globals

Definition
------------

We have seen in the :ref:`introduction` how to define a simple function with the following example::

    def compute_surface(radius):
        from math import pi
        return pi* radius * radius

To define a function, just precede the keyword **def** before the name of the function and add a column after it. The function definition is then followed by a block of statements.

The final line in the block of statement can start with the keyword **return** if you want to return something. If there is no return statement, the default behaviour of a function consists in returnintg the object **None**. So in the following function definition:: 

    i = 0
    def increment():
        global i
        i += 1

the function increments the global variable *i* and returns None (by default). See :ref:`globals` for more information.


Calls
------------

In order to call a function that returns a variable, type::

    surface = compute_surface(1.)

In order to call a function that returns nothing, just type::

    increment()

.. index:: nested

Misc
-------
You can write a function on a single line if the block statement is a simple compound statement::

    def sum(a, b): return a + b


Functions may be nested::


    def func1(a, b):

        def inner_func(x):
            return x*x*x

        return inner_func(a) + inner_func(b)

Functions are objects so you can assign a function to a variable name. See more on this subject in :ref:`assignfunc`.

See :ref:`namespace_scope` to see how scoping rules work in the context of nested functions.

.. index:: return

Return statement
=====================

Return a simple value
------------------------

You can use arguments to change input and therefore retrieve output of a function that way. However, usually it is more conveninent to use the **return** statement. We have already seen a few examples of the return statement. If you omit it, the function returns the None value.

Returning multiple values
--------------------------------

So far, we have seen functions returning either one value or none, which is actually one value (the Python object **None**). What about several values ? well, you can by returning a tuple of values. Technically, this is one object. Consider this example::

    def stats(data):
        """data must be a list of values"""
        _sum = sum(data) # note the underscore to avoid renaming the built-in function called sum
        mean = sum / float(len(data)) # note the usage of float function to avoid division by integer
        variance = sum([(x-mean(data))**2/len(data) for x in data])
        return mean, variance   # x,y syntax is a tuple ! 

    m, v = stats([1, 2, 1])

Arguments and Parameters
==========================

We have already seen how to pass 0, 1 or 2 arguments to a function. You can specify as many parameters as you want, however the numbers of arguments must be equal to the number of parameters. These parameters are the **positional arguments**.  Besides, Python provides a mechanism to specify **default values**, which can be provided by **keyword arguments**.

.. note:: A parameter is a name in the parameter list of a function definition's header. It receives a value from the caller of a function. An argument is the actual value or reference passed to a function by the caller. In::

        def sum(x, y):
            return x + y

    x and y are parameters whereas in the call::

        sum(1, 2)

    1 and 2 are arguments.


When you declare a function, parameters with default values must be provided before the positional arguments::

    >>> def compute_surface(radius, pi=3.14159):
    ...    return pi* radius * radius

and if you set an optional parameter then every parameters on its right must also be a default parameter. Therefore the following example is **WRONG**::

    >>> def compute_surface(radius=1, pi):
    ...    return pi* radius * radius

Now, for the calls, it works in a similar way. First positional arguments must be provided (all of them) and then optional arguments::

    >>> S = compute_surface(10, pi=3.14)

in fact the following call is also correct (you can specifically provide the positional name) but it is not common usage::

    >>> S = compute_surface(radius=10, pi=3.14)

However, this call is **incorrect**::

    >>> S = compute_surface(pi=3.14, 10)
    
When calling a function with default arguments, you can provide one argument or some and the order does not matter::

    >>> def compute_surface2(radius=1, pi=3.14159):
    ...    return pi* radius * radius
    >>> S = compute_surface2(radius=1, pi=3.14)
    >>> S = compute_surface2(pi=3.14, radius=10.)
    >>> S = compute_surface2(radius=10.)

You can also decide not to provide any keywords but then the order matters. It should correspond to the order of the parameters found in the definition::

    >>> S = compute_surface2(10., 3.14)
    >>> S = compute_surface2(10.)


If you decide not to use keywords, you must provide all arguments::

    def f(a=1,b=2, c=3):
        return a + b + c

You can not skip the second argument::

    f(1,,3)


If you want to circumvent this issue, you can use a dictionary::

   >>> params = {'a':10, 'b':20}
   >>> S = f(**params)


A default value is evaluated and saved only once when the function is defined (not when it is called).
Consequently, if a default value is mutable object such as a list or a dcitionary, it will change in-place over each function calls. If you want to avoid this behaviour, the initialisation must be done within the function or you should use an immutable object::

    >>> def inplace(x, mutable=[]):
            mutable.append(x)
            return mutable
    >>> res = inplace(1)
    >>> res = inplace(2)
    >>> print inplace(3)
    [1, 2, 3]

    >>> def inplace(x, lst=None):
            if lst is None: lst=[]
            lst.append()
            return lst

Another example of mutable argument modified in place is the following one::

    >>> def change_list(seq):
    ...    seq[0] = 100
    >>> original = [0, 1, 2]
    >>> change_list(lst1)
    >>> original
    [100, 1, 2]
 
To avoid the original sequence to be modified in-place a copy of the shared mutable object must be passed::

    >>> original = [0, 1, 2]
    >>> change_list(original[:])
    >>> original
    [0, 1, 2]





Specifying an arbitrary number of arguments
----------------------------------------------

Positional arguments
~~~~~~~~~~~~~~~~~~~~~
Sometimes, you may have a variable number of positional arguments. Examples of such functions are the :func:`max` and :func:`min` already presented earlier. The syntax to define such functions is::

    >>> def func(pos_params, *args):
    ...    block statememt


When you want to call the function, type::

    >>> func(pos_params, arg1, arg2, ...)


The way Python handle the provided arguments is to match the normal positional arguments from lzft to right and then places any other positional arguments in a tuple (\*args) that can be used by the function.

Consider the following function::

    >>> def add_mean(x, *data):
    ...    return x + sum(data)/float(len(data))

    >>> add_mean(10,0,1,2,-1,0,-1,1,2)
    10.5


If no excess arguments are provided, the default value is an empty tuple.


Arbitrary number of keyword arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Similarly to the positinal arguments, you can specify an arbitrary number of keyword arguments by using the following syntax (combined with the arbitrary number of optional arguments introduced in the previous section)::

    >>> def func(pos_params, *args, **kwargs):
    ...    block statememt

When you want to call the function, type::

    >>> func(pos_params, kw1=arg1, kw2=arg2, ...)

The way Python handles the provided keyword arguments is to match the normal positional arguments from left to right and then places any other positional arguments in a tuple (\*args) that can be used by the function  (sse previous section) and finally places any excess of keyword arguments in a dictionary (\*\*kwargs) that can be used by the function.



Consider the following function::

    >>> def print_mean_sequences(**kwargs):
    ...    def mean(data):
    ...        return sum(data)/float(len(data))
    ...    for k, v in kwargs.items():
    ...        print k, mean(v)

    >>> print_mean_sequences(x=[1,2,3], y=[3,3,0])
    y 2.0
    x 2.0


Note that you can also provide a dictionary but it has to be preceded by the double star ******::

    >>> print_mean_sequences(**{'x':[1,2,3], 'y':[3,3,0]})
    y 2.0
    x 2.0


Note also that the order of the output is not deterministic because a dictionary is not sorted!!



.. index:: docstring, __doc__

Documenting a function
========================

Let us define the following function::

    >>> def sum(s,y): return x + y

If you introspect the function, you will find a few hidden methods (starting with 2 underscores) amongst which the __doc__, that is used to set the documentation of a function. Python documentation are called **docstring** and can be put together with a function as follows::

    def sum(x, y):
        """This is a first line title

        Followed by a non-compulsary blank line and whatever text you 
        want to include. It may include sophistitated documentation 
        based on restructured syntax. 

        See http://thomas-cokelaer.info/tutorials/sphinx for more information.
        """
        return x+y 


The docstring must be the first statement after the function declaration. You can then extract the docstring easily (or complete it)::

    print sum.__doc__
    sum.__doc__ += "some additional text"

Methods, functions and attributes related to function objects
==================================================================

.. index:: __name__, __module__

If you introspect the available attributes of a function, you will find the following methods (everything is an object in Python even functions)::

    sum.func_closure   sum.func_defaults  sum.func_doc       sum.func_name
    sum.func_code      sum.func_dict      sum.func_globals   

And quite a few hidden methods, functions and attributes. For instance, you can also get the name of the function or the module where it is defined::

    >>> sum.__name__
    'sum'
    >>> sum.__module
    '__main__'

There are quite a few other methods and functions. Here is the list of those not discussed so far::


        sum.__call__          sum.__delattr__       sum.__getattribute__     sum.__setattr__
        sum.__class__         sum.__dict__          sum.__globals__       sum.__new__           sum.__sizeof__
        sum.__closure__       sum.__hash__          sum.__reduce__        sum.__str__
        sum.__code__          sum.__format__        sum.__init__          sum.__reduce_ex__     sum.__subclasshook__
        sum.__defaults__      sum.__get__           sum.__repr__          


Recursive functions
=====================


Recursion is not a Python property, it is a common technique in computer science where a function calls itself. The most common example is the factorial computation n! = n * n-1 * n-2 * ... 2 * 1. Knowing that 0! = 1, the factorial function can be written as::

    >>> def factorial(n):
    ...    if n != 0:
    ...        return n * factorial(n-1)
    ...    else:
    ...        return 1


Another common example (very well known in plant science) is the Fibonacci sequence defined as follows::

    f(0) = 1
    f(1) = 1
    f(n) = f(n-1) + f(n-2)

The recursive function can be written as::

    >>> def fibbonacci(n):
    ...    if n >= 2:
    ...        else:
    ...    return 1


The idea is that you must have a ending statement in your recursive function otherwise it will never ends. For instance the factorial implementation above is not robust. If you provide a negative value, it will call itself forever since there is no stop statement. We should rather write::

    >>> def factorial(n):
    ...    assert n > 0
    ...    if n != 0:
    ...        return n * factorial(n-1)
    ...    else:
    ...        return 1


.. warning:: recursive function allows you to write simple and elegant functions but speed and efficeincy is not guaranteed!


If a recursion is buggy (e.g. last forever), the function may run out of memory. You can retrieve or set the maximum number of recursion with the :mod:`sys` module. See :ref:`os_module` for more information.








.. index:: global

.. _globals:

global variable
===================

Here is again the example shown earlier that introduced global variable::

    i = 0
    def increment():
        global i
        i += 1

the function increments the global variable *i*. This is a way to modify a global variable defined outside of a function. Without it, this function would not know what is the variable **i**. The **global** keyword can appear anywhere but the variable can be used only after its declaration. 

Except rare case, you should not use global variables. 



.. _assignfunc:

Assigning a function to a variable
====================================

Given an existing function called *func*, the syntax is simply::

        variable = func

you can also assign built-in functions to variables. You can then call the function using another name. This technique is called **indirect function call**.

Reassigning alias is possible. Consider the following example::

    >>> def func(x): return x
    >>> a1 = func
    >>> a1(10)
    10
    >>> a2 = a1
    >>> a2()
    10

In this example, *a1*, *a2* and *func* have the same id. They all refer to the same object.

A practical example is when you want to refactor some code. for instance, you define a function called **sq** that computes the square of a value::

    >>> def sq(x): return x*x

later you want to rename it with a more meaningful name. The first option is to rename it. The issue is that if another piece of code uses the function call **sq** it will not work anymore. So, you could simply add this statement::

    >>> square = sq

A final example. Let us suppose that we reassign a built-in function as follows::

    >>> dir = 3

Then, we cannot access to the built-in function anymore, which may be an issue. To get back the built-in function, simply delete the variable::

    >>> del dir
    >>> dir()

.. index:: lambda

Anonymous function: the lambda keywork
=========================================

Lambda function are short one-line functions that have no name. They can contain only one statement so for instance the if, for and while are not allowed. They can be assigned to a variable (not compulsary)::

    product = lambda x,y: x*y

Note that unlike function, there is no **return** keyword used. The returned object is the result of the statement. 

Using :func:`type`, you can check its type::

    >>> type(product)
    function

See :ref:`lambda` for more examples. 
lambda is an expression whereas def is a statement.


lambda are not needed in practice. However, it is an elegant way of writing code in some particular cases where functions are short. 

You can also use default parameters and keywords like normal functions::

    >>> power = lambda x=1, y=2: x**y
    >>> square = power
    >>> square(5.)
    25


    >>> power = lambda x,y,pow=2: x**pow + y
    >>> [power(x,2, 3) for x in [0,1,2]]
    [2, 3, 10]


mutable default arguments
================================


::

    >>> def foo(x=[]):
    ...     x.append(1)
    ...     print x
    ... 
    >>> foo()
    [1]
    >>> foo()
    [1, 1]
    >>> foo()
    [1, 1, 1]

Instead, you should use a sentinel value denoting "not given" and replace with the mutable you'd like as default:

    >>> def foo(x=None):
    ...     if x is None:
    ...         x = []
    ...     x.append(1)
    ...     print x
    >>> foo()
    [1]
    >>> foo()
    [1]
