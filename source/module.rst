

.. index:: module, import, dir, copy, reload, dreload

.. _docmodule:

Module
######

In Python, a module is a file that contains python code with functions, classes or just variables.

We already introduced modules in the :ref:`basics_module` section. 

We will cover modules more in depth in this section but let us briefly remind how to import a module.


Quick start: how to import a standard module
============================================

In order to import a module, use the **import** keyword as follows::

    >>> import sys
    >>> import os

You can import several modules on the same line::

    >>> import sys, os

Modules contain functions, classes, variables, other modules... To access module's attribute (and more generally object's attributes), *qualify* the attribute with the object name by using the dot operator::

    >>> object.attribute

Sometimes, you may want to import only a particular function::

    >>> from sys import path

or all the functions but without importing the module itself::

    >>> from sys import *

This method is not adviced because you import everything and therefore increase the possiblity to 
import function with same names as those in your scope. See :ref:`module_design` for a solution.

You may find convenient to import a module with a different name::

    >>> import math as maths

.. note:: although **as** is a keyword, it can be used only with **import**.


There are a lots of standard modules provided with Python. However, you can easily creates your own modules (non  *standard* modules).


How to create and import your modules
=========================================

It works exactly as for the standard modules. You create a file, put some python code in it, open a python shell and type::

    import mymod

However, be aware that the Python interpreter looks in the directories that are part of the module search path defined by an environmental variable (PYTHONPATH under linux). You can check its contents within a Python shell with ::

    import sys
    print sys.path


You can also modify it within python by adding an existing path to it::

    import sys
    sys.path.append("newpath")

.. seealso:: :ref:`pythonpath`


Contents of a module
========================

The :func:`dir` function allows to find the functionalities provided by a module. Let us for instance introspect the content of the standard module :mod:`copy`::

    >>> import copy
    >>> dir_list = [name for name in dir(copy) if name[0]!='_']
    ['Error', 'PyStringMap', 'copy', 'deepcopy', 'dispatch_table', 
    'error', 'name', 't', 'weakref']

See more about the :mod:`copy` in :ref:`module_copy` section.

.. index:: __name__

Module's name
================

When you import a module, it contains a special attribute called `__name__`, which contains the name of the module::

    >>> import math
    >>> math.__name__
    'math'

Note, however, that within a module (or when you call the module with python executable) then the attribute `__name__` contains the value `"__main__"`. So, you could include the following code to make a Python module executable::

    if __name__ == "__main__":
        # run something.
        # you could call a function for instance.

This feature is useful when using test suite or if you want to create an executable.
When you run the module directly, __name__ is __main__, so the test suite executes. When you import the module, __name__ is something else, so the test suite is ignored. This makes it easier to develop and debug new modules before integrating them into a larger program.

.. note:: On Mac, there is an additional step to make the if __name__ trick work: pop up the module's options menu by clicking the black triangle in the upper-right corner of the windows and make sure Run as __main__ is checked


.. index:: __module__

Special function related to modules
====================================

* The :attr:`sys.modules` attribute returns the list of modules that have been imported in your session.
* Each class and function has a `__module__` attribute that returns the name of the module in which the class is defined.

.. index:: module, import, __all__

.. _module_design:

Module design and special attributes
======================================

You have quite a lot of freedom on the organisation of your module. 

You can add functions, classes, variables, other modules, documentation.

Here is an example of a module that we call **mymod**:


.. code-block:: python 
    :linenos:

    #!/usr/bin/python
    """Some documentation should be added on the top of the module"""

    # Then you import modules (could be elsewhere but traditionally it is on the top)
    import math

    __all__ = ["A", "welcome"]

    some_variable = 1
    _var = 2

    class A(object):
        """example of class"""
        pass

    class internal(object):
        """example of internal class"""
        pass

    def welcome(x):
        print("Hello")
    
    if __name__ = "__main__":
        welcome() 



Note that an empty module is perfectly valid: everything is optional. 

The first line include what is called **shebang** line. It is not needed under Windows or Mac system but could be used under Linux if you want the file to be an executable to specifically indicate where is the python executable. If so, it must be the first line of the module.




The string on the top is the documentation of the module. It must be either on the top or just below the **shebang**. It will populate the special attribute **__doc__**. When you type::

    >>> mymod?

this docstring will be shown.

The **__all__** statement (line 6) is optional. It defines the API (public functionalities of the module). When you type::

    from mymod import *

you import all the classes, functions and variables (except those starting with an underscore). However, at the beginning of the module, you can specify what should be the public part of the module using::

    __all__ = ["A", "welcome"]

This variable can be found when importing the module::

    >>> import mymod
    >>> mymod.__all__ 
    ["A", "welcome"]

In such case, only these names are imported. You can still access to a non-public functionality given its name by typing::

    from mymod import internal

There are other special attributes that could be useful:

* ``__file__`` returns the physical name of the module.
* ``__package__`` returns the package to which the module belongs.
* ``__doc__``  returns the docstring at the top of the module if any
* ``__dict__`` returns the entire scope of the module

An empty modules contains these 4 attributes and the __builtins__ attributes.

.. index:: import

More about importing module
============================

Although *import* can appear anywhere in the module, it is customary to add them at the top of the module;

You can import several modules on the same liner. These statements are correct::

    import sys
    import os, math


Once a module is imported, Python creates a variable for this module and another import will have no effect::

    >>> import math
    >>> math.pi = 3
    >>> import math # no effect
    >>> math.pi
    3

You can overcome this problem by using the reload/dreload functions (see next section :ref:`reload and dreload`)


You can load a specific attributes using **from**::

    from math import pi

you can import several names::

   from math import pi, cos, sin

and again, you can import all the attributes::

    from math import *

This statement can be used only on top of the module, not within a class or function definitions.

You should use **from** with cautious especially the last statement. **from** does not create a module object. It only copies the objects. You can not refer to the module. Instead, you should use **import**. As for the *import* case, **from** execustes the code only once. So, ::

    >>> from math import pi
    >>> pi = 3
    >>> from math import pi
    >>> pi
    3.141592653589793





.. index:: reload, dreload

.. _reload: 


reload and dreload
===================

When developping new code, it is not uncommon to import a module in a Python session, 
to change the code and want to use it without quitting the session. In other words, you want to reload the module or function. The ``reload()`` function does that for you. It imports a previously imported module again::

   reload(module_name)


Note that *module_name* is the name of the module you want to reload and not the string con-
taining the module name. The module name should be named **module_name** and not **module_name**.


.. warning:: reload() will load only the module that has been loaded fully and not those imported with a from-import statement.

Since a module also import other modules, you may need to perform a deep reload::

    dreload(module_name)


intra-packages reference
===========================
.. todo:: to be completed


.. doctest::
   :options: +SKIP

    >>> from . import echo
    >>> from .. import formats
    >>> from .. filters import equalizer


misc
==============

.. todo:: See builtins function called :func:`__module__` to override the default behaviour of the import function.

You can *attach* a variable to a module or function::

    def square(x):
       return x * x
    square.info = "simple square function"

You can use **as** several times on the same line::

    >>> import math as m, sys as s

You can combine *from*, *import* and *as*::

    from math import pi as constant_pi
