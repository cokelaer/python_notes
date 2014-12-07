shutil module
#################

:status: In progress 

The shutil module contains functions for operating on files. You might have noticed that ``os`` module also contains a function for renaming or moving files, (os.rename). Generally, you should use ``shutil.move`` instead, because it is more robust/complete than os.rename. 


Quick start
=============

You can use the function :func:`shutil.move` to rename a file::

     >>> import shutil
     >>> shutil.move("server.log", "server.log.backup")
     >>> shutil.move("image.png", "/home/user/")

and :func:`shutil.copy` to copy a file::

     >>> shutil.copy("image.png", "/home/user/")

it contains aliases to the module ``os`` and ``sys`` and ``collections``::

    >>> import shutil
    >>> shutil.os


If you want to delete a non-empty directory, use :func:`shutil.rmtree` (with cautious).


todo
=====
::

    shutil.abspath                    
    shutil.ignore_patterns            
    shutil.stat
    shutil.fnmatch
    shutil.copy2                     
    shutil.copyfile    
    shutil.copyfileobj 
    shutil.copymode                   
    shutil.copystat                   
    shutil.getgrnam  
    shutil.copytree    
    shutil.getpwnam 
    shutil.Error                      
    shutil.ExecError                  
    shutil.make_archive
    shutil.SpecialFileError           
    shutil.WindowsError               
    shutil.errno                      
    shutil.register_archive_format
    shutil.get_archive_formats      
    shutil.unregister_archive_format


