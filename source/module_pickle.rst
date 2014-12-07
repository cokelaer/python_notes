.. _module_pickle:

The pickle module
####################

:Status: in progress


Python provides the ``pickle`` module to store any Python object in a file and get it back later on. This is called storing the object ``persistently``.In fact there is also a module called ``cPickle``, which is simply faster and works the same way as ``pickle``.

.. note:: in other languages, pickling may be called with other names such as *serializing* or *marshalling*.

Quick start
=============

::

    >>> import cPickle as p
    >>> a = ['test', 1, {'key1':[1,2,3,4]}]
    >>> f = file('/tmp/data', 'w')
    >>> p.dump(a, f)
    >>> f.close()

    >>> del a
    >>> f = file('/tmp/data')
    >>> new_a = p.load(f)
    >>> print new_a
    ['test', 1, {'key1':[1,2,3,4]}]


You can pickle, None, numbers, strings, list, tuples, dictionaries, functions defined at top level, built-in functions, calsses defined at top-levels, instances of classes defined at top level of a  module.


Pickler and UnPickler are classes available in the pickle ,module. Note, however that they can be subclasses whereas the in cPickle they are functions. 


Remarks
===========

from [Norton]_

* Not all Python objects can be pickled. For instance, you can pickle a class instance, but the 
  class itself must be available when you unpickle the object. This isn't a problem for instances 
  of classes in standard Python modules, but if you pickle an instance of a class you wrote, make
  sure that the module containing that class is available when you unpickle. 
  The class itself isn't pickled. You don't have to import the module containing the class. 
  Python does this for you, as long as the module is available.
* Other types of objects may or may not be pickleable. An instance of an extension type (see
  Chapter 17) generally cannot be pickled, unless specialized pickling functions are available for
  that extension type. This includes some types in the standard Python modules.
* Pickles are portable between operating systems and architectures. For example, you can create a
  pickle on a Windows or GNU/Linux PC and unpickle it on a Mac, or even a Sun workstation.
  This enables you to move pickle files and transfer pickles over a network between different
  types of computers.
* Pickles are Python-specific. There's no easy way to access the contents of a pickle with programs written in other languages.

from [Fehily]_

* if you pickle a container (e.g. list) that contains aliases that refer to the same object, the items in the unpickeled object will still be aliases. 



todo
======

::

    
    
    pickle.dispatch_table        
    pickle.HIGHEST_PROTOCOL      
    pickle.StringIO
    pickle.StringTypes
    pickle.struct
    TracebackType
    pickle.encode_long          
    PicklingError         
    pickle.loads                 
    pickle.re                    
    pickle.classmap              
    pickle.marshal               
    pickle.UnpicklingError
    pickle.format_version        
    pickle.decode_long           
    pickle.whichmodule
    pickle.mloads                

cpickle todo
===============
::

    cPickle.dump                
    cPickle.dumps               
    cPickle.load                
    cPickle.PicklingError       
    cPickle.compatible_formats  
    cPickle.loads               
    cPickle.UnpickleableError
    cPickle.format_version      


