.. _slots:

slots
#######

**slots** provide a  special mechanism to reduce the size of objects. It is especially useful if you need to allocate thousands of objects that would otherwise take lots of memory space. It is not very common but you may find it useful someday. Note, however, that it has some side effects (e.g. pickle may not work) and that Python 3 introduced memory optimisation on objects (sse http://www.python.org/dev/peps/pep-0412/) so **slots** may not be needed anymore ?

The main idea is as follows. As you may know every object in Python contains a dynamic dictionary that allows adding attributes. You can see the slots as the static version that does not allow additional attributes. 

.. contents::


.. index:: slots

Quick Example
====================

Syntax
------------

Here is the **slots** syntax uing the **__slot__** keyword:

.. doctest::

    >>> class myClass(object):
    ...     __slots__ = ('x', 'y') #defining the slots.
    ...     def __init__(self, *args, **kwargs):
    ...         # initializing the values
    ...         self.x = 1
    ...         self.y = 2
    ...
    >>> a = myClass()
    >>> a.__slots__
    ('x', 'y')
    >>> a.__dict__ # A SLOT is not a dict so has no __dict__ !!!!!
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'myClass' object has no attribute '__dict__'
    >>> a.x
    1
    >>> a.y
    2   


Explanation
-----------------


The traditional version would be as follows:

.. doctest::

    >>> class myClass(object):
    ...     def __init__(self, *args, **kwargs):
    ...             self.x = 1
    ...             self.y = 2
    ...
    >>> instance = myClass()
    >>> instance.__dict__
    {'y': 2, 'x': 1}
    >>>

This means that for every instance you’ll have an instance of a dict. Now, for some people this might seem way too much space for just a couple of attributes.



More about sots
=========================

Unfortunately there is a side effect to slots. They change the behavior of the objects that have slots in a way that can be abused by control freaks and static typing weenies. This is bad, because the control freaks should be abusing the metaclasses and the static typing weenies should be abusing decorators, since in Python, there should be only one obvious way of doing something.

Making CPython smart enough to handle saving space without __slots__ is a major undertaking, which is probably why it is not on the list of changes for P3k (yet).

    
I'd like to see some elaboration on the "static typing"/decorator point, sans pejoratives. Quoting absent third parties is unhelpful. __slots__ doesn't address the same issues as static typing. For example, in C++, it is not the declaration of a member variable is being restricted, it is the assignment of an unintended type (and compiler enforced) to that variable. I'm not condoning the use of __slots__, just interested in the conversation. Thanks! – hiwaylon Nov 28 '11 at 17:54
1    
    

Each python object has a __dict__ atttribute which is a dictionary containing all other attributes. e.g. when you type self.attr python is actually doing self.__dict__['attr']. As you can imagine using a dictionary to store attribute takes some extra space & time for accessing it.

However, when you use __slots__, any object created for that class won't have a __dict__ attribute. Instead, all attribute access is done directly via pointers.

So if want a C style structure rather than a full fledged class you can use __slots__ for compacting size of the objects & reducing attribute access time. A good example is a Point class containing attributes x & y. If you are going to have a lot of points, you can try using __slots__ in order to conserve some memory.
    
No, an instance of a class with __slots__ defined is not like a C-style structure. There is a class-level dictionary mapping attribute names to indexes, otherwise the following would not be possible: class A(object): __slots__= "value",\n\na=A(); setattr(a, 'value', 1) I really think this answer should be clarified (I can do that if you want). Also, I'm not certain that instance.__hidden_attributes[instance.__class__[attrname]] is faster than instance.__dict__[attrname]. – tzot Oct 15 '11 at 13:56
up vote 4 down vote
    

Slots are very useful for library calls to eliminate the "named method dispatch" when making function calls. This is mentioned in the SWIG documentation. For high performance libraries that want to reduce function overhead for commonly called functions using slots is much faster.

Now this may not be directly related to the OPs question. It is related more to building extensions than it does to using the slots syntax on an object. But it does help complete the picture for the usage of slots and some of the reasoning behind them.


By default, instances of both old and new-style classes have a dictionary for attribute storage. This wastes space for objects having very few instance variables. The space consumption can become acute when creating large numbers of instances.

The default can be overridden by defining __slots__ in a new-style class definition. The __slots__ declaration takes a sequence of instance variables and reserves just enough space in each instance to hold a value for each variable. Space is saved because __dict__ is not created for each instance.

This class variable can be assigned a string, iterable, or sequence of strings with variable names used by instances. If defined in a new-style class, __slots__ reserves space for the declared variables and prevents the automatic creation of __dict__ and __weakref__ for each instance. New in version 2.2. 



Notes on using __slots__

    Without a __dict__ variable, instances cannot be assigned new variables not listed in the __slots__ definition. Attempts to assign to an unlisted variable name raises AttributeError. If dynamic assignment of new variables is desired, then add '__dict__' to the sequence of strings in the __slots__ declaration. Changed in version 2.3: Previously, adding '__dict__' to the __slots__ declaration would not enable the assignment of new attributes not specifically listed in the sequence of instance variable names.

    Without a __weakref__ variable for each instance, classes defining __slots__ do not support weak references to its instances. If weak reference support is needed, then add '__weakref__' to the sequence of strings in the __slots__ declaration. Changed in version 2.3: Previously, adding '__weakref__' to the __slots__ declaration would not enable support for weak references.

    __slots__ are implemented at the class level by creating descriptors (3.4.2) for each variable name. As a result, class attributes cannot be used to set default values for instance variables defined by __slots__; otherwise, the class attribute would overwrite the descriptor assignment.

    If a class defines a slot also defined in a base class, the instance variable defined by the base class slot is inaccessible (except by retrieving its descriptor directly from the base class). This renders the meaning of the program undefined. In the future, a check may be added to prevent this.

.. warning:: effects of a __slots__ declaration is limited to the class where it is defined. In other words, subclasses will have a __dict__ (unless they also define __slots__).


    __slots__ do not work for classes derived from ``variable-length'' built-in types such as long, str and tuple.

    Any non-string iterable may be assigned to __slots__. Mappings may also be used; however, in the future, special meaning may be assigned to the values corresponding to each key.


For every instance of any class, attributes are stored in a dictionary.
   
.. doctest::

    >>> class myClass(object):
    ...     def __init__(self, *args, **kwargs):
    ...             self.x = 1
    ...             self.y = 2
    ...
    >>> instance = myClass()
    >>> instance.__dict__
    {'y': 2, 'x': 1}
    >>>

This means that for every instance you’ll have an instance of a dict. Now, for some people this might seem way too much space for just a couple of attributes.

If you have lots and lots and looooots of instances, and you want to save some memory, you can use __slots__. The basic idea is that when you define the __slots__ class attribute, those attributes will get just the enough space, without wasting space.

Here is the previous example using __slots__::
    
    >>> class myClass(object):
    ...     __slots__ = ('x', 'y') #defining the slots.
    ...     def __init__(self, *args, **kwargs):
    ...             # initializing the values
    ...             self.x = 1
    ...             self.y = 2
    ...
    >>> instance = myClass()
    >>> instance.__slots__
    ('x', 'y')
    >>> instance.__dict__ # NO __DICT__ !!!!!
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'myClass' object has no attribute '__dict__'
    >>> instance.x
    1
    >>> instance.y
    2   
    No __dict__ !

Now, one side effect of these __slots__ thing is that, whenever you define the __slots__ class attribute, your __dict__ attribute for every instance will be gone!. It’s not a surprise because that’s why you should use __slots__ in the first place… to get rid off the __dict__ in every instance, to save some memory remember?
Can’t bind attributes to the instance any more…

Another side effect is that, as there is no __dict__, there is no way to add, at runtime, any attributes to your instance:

    
# This should should work if there is no __slots__ defined...
>>> instance.new_attr = 10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'myClass' object has no attribute 'new_attr'
>>>
Read only attributes?

Another one is that, if there is some kind of collision between the slot and a class attribute, then the class attribute will overwrite the slot and, as there is no __dict__, the class attribute will be read-only.

::
    
    >>> class myClass(object):
    ...     __slots__ = ('x', 'y')
    ...     x = 10
    ...     def __init__(self,*args, **kwargs):
    ...             self.y = 2
    ...
    >>> instance = myClass()
    >>> instance.x
    10
    >>> instance.x = 2
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    AttributeError: 'myClass' object attribute 'x' is read-only
    >>> instance.y
    2
    >>> instance.y = 3
    >>> instance.y
    3
    >>> instance_2 = myClass()
    >>> instance_2.x
    10
    >>> instance_2.y = 100
    >>> instance.y
    3
    >>> instance_2.y
    100
    >>>      

However if you want to have a __dict__, you can always insert into the __slots__ the ‘__dict__’ value, and all these little side effects will go away
::
    
    <pre>>>> class myClass(object):
    ...     __slots__ = ('x', 'y', '__dict__')
    ...     x = 10
    ...     def __init__(self, *args, **kwargs):
    ...             self.y = 2
    ...
    >>> instance = myClass()
    >>> instance.x
    10
    >>> instance.x = 100
    >>> instance.x
    100
    >>> instance.y
    2
    >>> instance.__dict__
    {'x': 100}
    >>> instance.__slots__
    ('x', 'y', '__dict__')
    >>>

But what if I wanted to add the ‘__dict__’ value into __slots__ at runtime?

sorry dude but, no can do.

::

    >>> class myClass(object):
    ...     __slots__ = ('x')
    ...     def __init__(self, *args, **kwargs):
    ...             self.x = 1
    ...
    >>> a = myClass()
    >>> a.x
    1
    >>> a.__slots__
    'x'
    >>> a.__slots__ = ('x', 'y')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'myClass' object attribute '__slots__' is read-only
    >>>



reference: http://mypythonnotes.wordpress.com/2008/09/04/__slots__/:wq

