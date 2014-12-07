.. _classes:

Classes
########

In python everything is an object. In other words everything is an instance of a class. We cover in this section different aspects of classes and object oriented approach available in Python. Before, let us summarize the characteristics of objects. Objects

 * can store data
 * are instances of python classes
 * are created by an expression
 * can be referenced by one or more variable
 * have a unique identifier returned by :func:`id`
 * are mutable or immutable depending on the type (e.g., list vs tuple)
 * can be converted to string using :func:`str`
 * can be printed
 * are deleted automatically when no longer needed

.. index:: object, isinstance, issubclass, __dict__, __name__, __docstring__

Simplest class example
------------------------

The following example defines a class ``Simplest`` that contains nothing. Then, we create an instance ``s``.

::

    class Simplest(object): 
        """simple class prototype"""
        pass

Note that all classes since version 2.2 should inherit from :func:`object`, which is the most base type. In eqrlier version, the syntas was::

    class OldStyle:
        """simple class prototype"""
        pass

You may still use this syntax or see it in code here and there. However, we will not use it.       
The way to create an instance is simply::

    s = Simplest()

you add attributes dynamically::

    s.attribute = 1

This very simple class has no interest except to show the syntax of instanciation. The way we added attribute here above is dynamic. If you need it in all instances, it would be better to add it directly in the class definition as shown later on.

You can already introspect the instance since it contains hidden special fields: **__doc__** and **__module__**. The first contains what we provided in our code as a docstring: "simple class prototype". The second one contains the string "__main__". See :ref:`modules` for more details about the __module__ field.

You can check that **s** is indeed an instance of **simplest**::

    >>> isinstance(s, Simplest)
    True

and that Simplest is a sub class of **object**::

    >>> issubclass(Simplest, object)
    True

There is also a hidden attribute called __dict__ that gives you all the attributes of a class defined so far in the form of a dictionary::

    >>> s.__dict__
    {'attribute': 1}

as well as the name of the class::

    >>> s.__name__
    "Simplest"

There are quite a few other special attributes that we will discover later in this section.

.. todo::

        s.__format__        s.__module__              s.__subclasshook__
        s.__delattr__       s.__getattribute__  s.__new__           s.__setattr__       s.__weakref__
        s.__hash__          s.__reduce__        s.__sizeof__        
        s.__reduce_ex__      


Constructor
------------

Constructor are optional. However, most of the time you would require it and is defined using the special method `__init__` . 

Here is a simple Range class that behaves like the built-in :func:`range` function but with a constant step of 1. We could have inherited from range but we will see inheritance later on. For now, let us design the class to show how to use a constructor with the special method __init__::

    class Range(object):
        def __init__(self, start=0, end=10):
            self.counter = start
            self.end = end

        def next(self):
            if self.counter < self.end:
                res = self.counter
                self.counter += 1
                return res
            else:
                return None # optional 

As you can see the constructor has 3 arguments. The first one is used by Python. It is like **this** keyword in C++. It refers to the class itself and is compulsary. **self** is not a keyword, it is just a parameter. You could call it **this** and the syntax would be perfectly correct. However, you should name it **self** since it is the custom followed by everybody writting Python code.


The 2 other arguments are the user arguments provided during an instanciation. Like functions, arguments can be optional or not (see :ref:`functions`)::

    c = Range(5, 10)
    c = Range(end=10)





Class and instance variables
--------------------------------

Here is a simple class in Python that illustrate the difference between a **class variable** and
an **instance variable**:: 

    class MyClass(object):
        counter = 0
        def __init__(self, arg1)
            self.arg1 = arg1
            counter = counter + 1
        def __str__(self):
            return 'There are %d instances of MyClass' % self.counter

counter is a **class variable** shared by all instances::

    >>> c1 = MyClass(1)
    >>> c2 = MyClass(2)
    >>> print c1
    'There are 2 instances of MyClass'
    >>> c2.counter
    2


All class members (including the data members) are public and all the methods are virtual in Python.

Inside a class definition, all names beginning with two leading underscores are translated by
adding a single underscore and the class name to the beginning:

.. doctest::

    >>> MyClass._MyClass__privateVariable #doctest: +SKIP

Although the double underscores seems like a standard private method, it is not since, we can still access to it using the `_MyClass` prefix. So, if you know how this works behind the scene, it is still possible to access private methods outside the class, even though you're not supposed to.

.. note:: If you don't want the name-mangling effect, but you still want to send a signal for other objects to stay away, you can use a single initial underscore.


Inheritance
----------------


In order to inherit fro, an existing class, use the following syntax::

    class Animal(object):
        def __init__(self, name="unknown"):
            self.name = name
        def __str__(self):
            print("I'm a {0}".format(self.name))

    def Cat(Animal):
        def __init__(self):
            super().__init__(name='CAT')

Here, the parent's class `Animal` is initialised inside the child class  using the super keyword.
The Cat inherits from Animal and therefore has the method **print** already available.




Multiple inheritance
--------------------------


if Python cannot find a variable or method in the local namespace, it will perform a depth first search of the super classes in the same order in which the superclasses are specified in the class definition.

That's all you need to know !! Let us study an example::


    class Vehicle(object):
        def __init__(self, name, color, wheel):
            self.name = name
            self.wheels = None
            self.color = None

        def set_wheels(self, n):
              self.wheels = 2

        def __str__(self):
            txt = str(self.name) + ":" + registration
            return txt

    class TwoWheeler(object):

        def __init__(self, name, color):
            self.name = name
            self.set_wheels(2)
            self.color = None

        def __str__(self):
            return  self.wheels

    class MotorVehicle(object):

        def __init__(self, name, color, power):
            self.name = name
            self.set_wheels(2)
            self.color = None
            self.power

    class Bicycle(TwoWheeler, gear):

        def __init__(self, name, color, gear):
            self.name = name
            self.set_wheels(2)
            self.color = None





.. index:: diamond inheritance


Diamond inheritance
-----------------------------

Example before but a TwoWheeler and MotorVehicle both inherit from the vehicle. In Python, looking for a method or attribute from vehicle follows the rule introiduced in section xx so Python first look inside Twohwheeler then in Vehicle. So, the method os MotorVehcile is ignored if found before.



.. index:: iterator

The iterator method
-----------------------


::

    class Reverse(object):
        """Iterator for looping over a sequence backwards."""
        def __init__(self, data):
            self.data = data
            self.index = len(data)

        def __iter__(self):
            return self

        def next(self):
            if self.index == 0:
                raise StopIteration
            self.index = self.index - 1
            return self.data[self.index]

It can be used as follow::

    >>> rev = Reverse([1,2,3,4])
    >>> for x in rev: print x
    4
    3
    2
    1



Overloading standard behaviour
====================================

Overlaoding is the ability to have several functions with the same name but different set of parameters. This is possible on functions and metohods in languages such as C++. 

This is not possible for functions or methods  in Python. However, polymorphism is possible.

example: special method __str__ to create astring representation of an instance
----------------------------------------------------------------------------------

when calling str(x) on a list, Python invokes the special methoods __str__, which can be overloed. Let us create a new list class::


    class MyList(list):
        def __init__(self, x):
            list.__init__(self,x)

        def __str__(self):
            if len(self)>10:
                txt = "This list contains %s elements" % str(len(self))+"\n"
                this = []
                this.extend(self[0:5])
                this.extend(["..."])
                this.extend(self[-5:])
                txt += this.__str__()
            else:
                txt = list.__str__(self)
            return txt


::

    >>> m = MyList(range(0,100))
    >>> print(m)
    This list contains 100 elements
    [0, 1, 2, 3, 4, '...', 95, 96, 97, 98, 99]  
    >>> isinstance(m, list)
    True
    >>> isinstance(m, MyList)
    True



__str__: informal representation of an instance.
__repr__: formal representation of an instance.: returns a valid python expression that can be evaluated ti re-cerate an object with the same value.

.. index:: __del__


Destructor
--------------------

The __del__ method is rarely used in practice and there is a good reason for this: there's no guarantee that __del__ will be called in a specific time period. So it is no recommended to rely on this method. If you awnt to perform some cleanup, it is better to make your own cleanup function. 

Note that :func:`del` does not call __del__ . del decreases the reference counter and __del__ is called when the coutner is zero.

The way Python periodically reclaims block of memory that are no lpnger in use is termed garbage collection. The garbage collector is performed during program execution and triggered when an object's reference coutn reaches zero. You do not see when an instance is destroyed but the special method __del__ (desctrutor) is called at that moment. It is invoked only onece per instance. 


You can control the garbage collector with the mod:`gc` module. 

Reference countin fails when there are cycles:: 

   x = [1, 2, 3]
   y = x
   x = y

None of the refence counter will be wero s oneither will be collected . To cope with this situation, Python perdiocally runs a cycle-detection routine? The garbage collector does not collect cyclic instnces for which __del__ is defined. A good reason to not use that method.




. discuss about the gc moule and garbage collector




setting the truth value of an instance
------------------------------------------

You can ask whether an instance is true or false. by default an instance truth value is true but you can use __nonzero__ to return 0 or 1


If you do not define __nonzero__, Python invokes __len__(). if none are defined, te instaqnce is considered True.



comparing instances
------------------------

There are 6 specials methods related to comparison that can be overlaoded

===================== ======================
method                operator
===================== ======================
__lt__(self, other)   self < other
__le__(self, other)   self <= other
__gt__(self, other)   self > other
__ge__(self, other)   self >= other
__eq__(self, other)   self == other
__ne__(self, other)   self != other
===================== ======================

Here is an example with that redefine the __eq__::

   >>> class MyGraph():
           def __init__(self, nodes, edges):
               self.nodes = nodes[:]
               self.edges = edges[:]

           def __eq__(self, g):
               if sorted(self.nodes) != sorted(g.nodes):
                   return False
               if sorted(self.edges) != sorted(g.edges):
                   return False
               return True

    >>> g1 = MyGraph(['A','B','C'], edges=[('A','B'), ('B','C')])
    >>> g2 = MyGraph(['A','C','B'], edges=[('B','C'), ('A','B')])
    >>> g1 == g2
    True


These methods can return any object not just 1/0 or True/False.

In older version of Python, the __cmp__ method could be used. It should return a negative value if self<other, a zero if self==other and a positive value if self>other. If you define __cmp__, you should also define __hash__ to calculate an integer hash key to use in dictionary operations. 



Accessing instance attributes
--------------------------------



__getattr__is called only is an instance cannot be found in the __dict__ method that is it is neither an attribute nor a method. It should return an attribute value or raise an AttributeError exception.

__setattr__ invoket when you attempt to assign an attribute. if defined, it is invoked in place of the normal behaviour (storing the value in the instance dictionary). If you want to set an attribute, use self.__dict__[name] = value. self.name causes recursion error. 

See also the property hereafter that provide a nice mechanism to make attribute read-only. 

__delattr__ 


Example::


    class Simple(object):
        def __init__(self,x, y):
            self.x = x
            self.y = y


    class Tuned(object):
        def __init__(self):
            self._x = None
            self._y = None

        def __getattr__(self, name):
            if name =="x":
                return self._x
            if name =="y":
                return self._y

        def __setattr__(self, name, value):
            if value>=0:
                self.__dict__[name] = value
            else:
                raise ValueError("value must be positive.")

    t = Tuned()
    t.x = 1
    t.y = -1



differnce with getattr, setattr, delattr functions: 

=================== ======================
method              operator
=================== ======================
__lt__(self, other) self < other
__le__(self, other) self <= other
__gt__(self, other) self > other
__ge__(self, other) self >= other
__eq__(self, other) self == other
__ne__(self, other) self != other
=================== ======================

property
------------


.. todo:: 


Treating an instance like a list or dictionary
---------------------------------------------------

You can use special methods to make your class behave like sequences and dictionary with slicing, indexing and key loopkup. 


__len__ should return an integer greater than or equal to zero. If __nonzero__ is not defined, the value of __len__ is used to tell if the instance if True or False. 




__getitem__, __setitem__, and __delitem__ are used to define the behaviour or the brackets operator::

    a[0]
    a[0] = 1
    del a[0]


__delitem__ is called whenever you use the **del** keyword. 


__getslice__, __setslice__, __delslice__ are used to define the following operators::

    a[0:10]
    a[0:10] = range(0,10)
    del a[0:10] 

of course the setslice and delslice cannot be used for immutable sequences

__getslice__ should return the same type of sequence that it is passed.


__contains__ is called when you use the **in** keyword. 


Here is a summary

============================  ======================
method                        Description 
============================  ======================
__len__(self)                 returns len(self)
__getitem__(self, i)          return self[i]
__setitem__(self, i, value)   self <= other
__delitem__(self, i)          self > other
__getslice__(self, i, j)       self >= other
__setslice__(self, i, j)      self == other
__delslice__(self, i, j)      self != other
__contains__(self, item)      self != other
============================  ======================

dictionary and list should also implement  concatenation (addition) and repetition (multiplication) as well as mathematical methods. It is done by redefining the __add__, __radd__ ,__iadd__, __mul__, __rmul__, __imul__ methods.

 

Mathematical opertions on instance
-------------------------------------

The mathematical methods that can be implemented are provided in this section. Each mathematical operations has its method. For instance the binary operator methods take the folloing form::

    x + y

that is defined within your class as::

    x.__add__(y)

where **x** is the **self** of the method and **y** is a parameter.

The binary operator methods are summarized here below:

======================= ============================
methods                 Effets
======================= ============================
__add__(self, other)    self + other
__sub__(self, other)    self - other
__mul__(self, other)    self * other 
__div__(self, other)    self / other 
__mod__(self, other)    self % other
__divmod__(self, other) divmod(self, other)
__pow__(self, other)    self ** other
__lshift__(self, other) self << other
__rshift__(self, other) self >> oter
__and__(self, other)    self & other
__or__(self, other)     self | other
__xor__(self, other)    self ^ other
======================= ============================


Python also provides binary operator methods with reversed operands. There are used if the left operand does not support the operation. For instance in the operation::

    x + y

If x does not support the + operator, Python tries::

    y + x

by invoking::

    y.__radd__(x)

The list of reversed operator methods is the same as above with a **r** character added to its left.

======================== ============================
methods                  Effets
======================== ============================
__radd__(self, other)    other + self
__rsub__(self, other)    other - self 
__rmul__(self, other)    other * self 
__rdiv__(self, other)    other / self 
__rmod__(self, other)    other % self 
__rdivmod__(self, other) divmod(self, other)
__rpow__(self, other)    self ** other 
__rlshift__(self, other) other << self 
__rrshift__(self, other) other >> self 
__rand__(self, other)    other & self 
__ror__(self, other)     other | self 
__rxor__(self, other)    other & self 
======================== ============================

The in_place (or augmented) operator methods performs in place modifications of self and return the result. In ::

    x += y

Python tries to find ::

    x.__iadd__(y) 

If that method is not defined, then Python searches for ``x.__add__(y)`` and ``y.__radd__(x)`` as if `x+y` was invoked.

========================= ============================
methods                   Effets
========================= ============================
__iadd__(self, other)     self += other
__isub__(self, other)     self -= other  
__imul__(self, other)     self `*=` other 
__idiv__(self, other)     self /= other 
__imod__(self, other)     self %= other 
__ipow__(self, other)     self ``**=`` other 
__ilshift__(self, other)  self <<= other 
__irshift__(self, other)  self >>= other 
__iand__(self, other)     self &= other 
__ior__(self, other)      self `|=` other 
__ixor__(self, other)     self ^= other 
========================= ============================


Unary operator methods are also available


======================= ============================
methods                 Effets
======================= ============================
__neg__(self)           -self
__pos__(self)           +self
__abs__(self)           abs(self)
__invert__(self)        ~self
======================= ============================

Finally, conversion methods are the following ones. Note that oct and hex should return oct and hexadecimal strings. int, long; float, complex should convert values to the appropriate built-in type.
__coerce__ should follow the rules given in the Python Reference Manual.

========================= ============================
methods                   Effets
========================= ============================
__int__(self)             int(self)
__long__(self)            long(self)
__float__(self)           float(self)
__complex__(self)         complex(self)
__oct__(self)             oct(self)
__hex__(self)             hex(self)
__coerce__(self)          coerce(self)
========================= ============================

.. todo:: more examples ?

calling an instance
---------------------------

if __call__ is provided, you can call your instance::

    class Mode(object):
        def __init__(self, x):
            self.x = x
            self.mode = {}

        def __call__(self, mode):
            if mode == 1:
                return 
            elif mode == 2:
                return
            else:
                raise NotImplementedError
        
    mode = Mode()
    mean = mode(mode=1)
    variance = mode(mode=2)
    

.. todo:: check this example









