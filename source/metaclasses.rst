metaclasses
==============

metaclasses are to classes what classes are to instances:.

Here are the first things I found out:

    Not that important. Everybody, everywhere says not to use them unless absolutely necessary, whatever that means. Every time I read something on the internet regarding metaclasses, somewhere in there it said “but they are rarely used, and you should ask yourself if you really need them”.
        Metaclasses always inherits from type. Stupid, but I would think that there is some kind of analogy between everything inheriting from type and everything inheriting from object.
            The __init__ and __new__ are executed only once, that’s when the class is created. It is not executed when an instance of the class is created but only when the instance of the metaclass.
                Obviously, when you instance a metaclass, the instance is the class. This classes can access the metaclass meta-attributes, but the classes’s instances cannot do that. It’s like they are like… two different parallel worlds. On one hand you have the Metaclasses – Classes world and on the other hand you’ve got the Classes – Objects world. You can, by using some kind of non-standard way, move from one world to the other one, like black holes or sth. like that… =D.
                    The same thing happens with the meta-methods. The instances of the metaclass can call the metaclasse’s meta-method, but the class’es instances cannot.

                    In later posts I’ll try to understand more of these crazy beast, as well as find out where the heck they are used. (Django?)



:references: http://mypythonnotes.wordpress.com/2009/04/05/understanding-metaclasses/
