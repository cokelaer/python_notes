.. _os_module:

The os module (and sys, and path)
##################################

The :mod:`os` and :mod:`sys` modules provide numerous tools to deal with filenames, paths, directories. The :mod:`os` module contains two sub-modules :mod:`os.sys` (same as :mod:`sys`) and :mod:`os.path` that are dedicated to the system and directories; respectively. 

Whenever possible, you should use the functions provided by these modules for file, directory, and path manipulations. These modules are wrappers for platform-specific modules, so functions like **os.path.split** work on UNIX, Windows, Mac OS, and any other platform supported by Python. 


.. seealso:: These :mod:`shutil`, :mod:`tempfile`, :mod:`glob` modules from the Python documentation.

Quick start
=============

You can build multi-platform path using the proper separator symbol::

    >>> import os
    >>> import os.path
    >>> os.path.join(os.sep, 'home', 'user', 'work')
    '/home/user/work'

    >>> os.path.split('/usr/bin/python')
    ('/usr/bin', 'python')


Functions
===========

The **os** module has lots of functions. We will not cover all of them thoroughly but this could be a good start to use the module.

.. index:: getcwd, getcwdu, chdir, mkdir, makedirs

Manipulating Directories
-------------------------------

The :func:`~os.getcwd` function returns the current directory (in unicode format with :func:`~os.getcwdu` ).

The current directory can be changed using :func:`~os.chdir`::

    os.chdir(path)

The :func:`~os.listdir` function returns the content of a directory. Note, however, that it mixes directories and files.


The :func:`~os.mkdir` function creates a directory. It returns an error if the parent directory does not exist. If you want to create the parent directory as well, you should rather use :func:`~os.makedirs`::

    >>> os.mkdir('temp') # creates temp directory inside the current directory
    >>> os.makedirs(/tmp/temp/temp")

Once created, you can delete an **empty** directory with :func:`~os.rmdir`:

.. doctest::

    >>> import os
    >>> os.mkdir('/tmp/temp')
    >>> os.rmdir('/tmp/temp')

You can remove all directories within a directory (if there are not empty) by using :func:`os.removedirs`.

If you want to delete a non-empty directory, use :func:`shutil.rmtree` (with cautious).

Removing a file
-----------------

To remove a file, use :func:`os.remove`. It raise the OSError exception if the file cannot be removed. Under Linux, you can also use :func:`os.unlink`.

Renaming files or directories
----------------------------------

You can rename a file from an old name to a new one by using :func:`os.rename`. See also :func:`os.renames`.

Permission
----------------
you can change the mode of a file using :func:`chmod`. See also **chown**, **chroot**, **fchmod**, **fchown**.

The :func:`os.access` verifies the access permission specified in the mode argument. Returns 1 if the access is granted, 0 otherwise. The mode can be:

======== =====================================================
======== =====================================================
os.F_OK  Value to pass as the mode parameter of access() to 
         test the existence of path.
os.R_OK: Value to include in the mode parameter of access() 
         to test the readability of path.
os.W_OK  Value to include in the mode parameter of access() 
         to test the writability of path.
os.X_OK  Value to include in the mode parameter of access() 
         to determine if path can be 
======== =====================================================

::

    >>> os.access("validFile", os.F_OK)
    True

You can change the mask of a file using the the :func:`os.umask` function. The mask is just a number that summarises the permissions of a file::

    os.umask(644)


Using more than one process
--------------------------------

On Unix systems, :func:`os.fork` tells the computer to copy everything about the currently running program into a newly created program that is separated, but almost entirely identical. The newly created process is the **child process** and gets the data and code of the parent process. The child process gets a process number known as **pid**. The parent and child processes are independent.

The following code works on Unix and Unix-like systems only::

       import os
       pid = os.fork()
       if pid == 0: # the child
            print "this is the child"
       elif pid > 0:
            print "the child is pid %d" % pid
       else:
           print("An error occured")

       
Here, the fork is zithin the executed script but ,ost of the time; you would require the 




One of the most common things to do after an os.fork call is to call os.execl immediately afterward
to run another program. os.execl is an instruction to replace the running program with a new program, so the calling program goes away, and a new program appears in its place::

    import os
    pid = os.fork()
    # fork and exec together
    print "second test"
    if pid == 0: # This is the child
        print "this is the child"
        print "I'm going to exec another program now"
        os.execl(`/bin/cat', `cat', `/etc/motd')
    else:
        print "the child is pid %d" % pid
        os.wait()


The os.wait function instructs Python that you want the parent to not do anything until the child process returns. It is very useful to know how this works because it works well only under Unix and Unix-like platforms such as Linux. Windows also has a mechanism for starting up new processes.
To make the common task of starting a new program easier, Python offers a single family of functions that combines os.fork and os.exec on Unix-like systems, and enables you to do something similar on Windows platforms. When you want to just start up a new program, you can use the os.spawn family of functions. 

The different between the different spawn versions:

    * `v` requires a list/vector os parameters. This allows a command to be run with very different commands from one instance to the next without needing to alter the program at all.
    * `l` requires a simple list of parameters. 
    * `e` requires a dictionary containing names and values to replace the current environment. 
    * `p` requires the value of the PATH key in the environment dictionary to find the program. The

p variants are available only on Unix-like platforms. The least of what this means is that on Windows
your programs must have a completely qualified path to be usable by the os.spawn calls, or you have to
search the path yourself:

::

     import os, sys
     if sys.platform == `win32':
          print "Running on a windows platform"
          command = "C:\\winnt\\system32\\cmd.exe"
          params = []
     if sys.platform == `linux2':
          print "Running on a Linux system, identified by %s" % sys.platform
          command = `/bin/uname'
          params = [`uname', `-a']
     print "Running %s" % command
     os.spawnv(os.P_WAIT, command, params)


The exec function comes in different flavours: 

* execl(path, args) or execle(path, args, env) env is a dict with env variables. 
* exexp(file; a1; a2, a3) or  exexp(file; a1; a2, a3, env) 


.. Not done
.. lseek, stat_result

.. topic:: todo

    ::

        os.getloadavg              os.setegid
        os.getlogin                os.seteuid
        os.abort                   os.getpgid                 os.setgid
        os.getpgrp                 os.setgroups
        os.setpgid                 os.setpgrp
        os.UserDict                os.getresgid               os.setregid
        os.getresuid               os.setresgid               os.getsid
        os.setresuid               os.setreuid
        os.closerange              os.initgroups              os.setsid
        os.confstr                 os.isatty                  os.setuid
        os.confstr_names           os.ctermid                
        os.defpath                 os.devnull                 
        os.link                    os.dup                     os.dup2    
        os.errno        os.major 
        os.error                   os.makedev                 os.stat_float_times
        os.execl           
        os.execle                  os.minor                   os.statvfs
        os.execlp                  os.statvfs_result
        os.execlpe                 os.mkfifo                  os.strerror
        os.execv                   os.mknod                   os.symlink
        os.execve                  
        os.execvp                  os.sysconf
        os.execvpe                 os.open                    os.sysconf_names
        os.extsep                  os.openpty                 os.system
        os.fchdir                  os.pardir                  os.tcgetpgrp
        os.tcsetpgrp    os.pathconf                os.tempnam
        os.fdatasync               os.pathconf_names          os.times
        os.fdopen                  os.tmpfile
        os.pipe                    os.tmpnam
        os.forkpty                 os.popen                   os.ttyname
        os.fpathconf               os.popen2                  os.popen3                  
        os.fstatvfs                os.popen4                 
        os.fsync                   os.putenv                  os.unsetenv
        os.ftruncate               os.read                    os.urandom
        os.readlink                os.utime            
        os.wait                    os.wait3
        os.getenv                  os.wait4              
        os.waitpid                os.getgroups 


The :func:`os.walk` function allows to recursively scan a directory and obtain tuples containing tuples of (dirpath, dirnames, filename) where dirnames is a list of directories found in dirpath, and filenames the list of files found in dirpath.

Alternatevely, the os.path.walk can also be used but works in a different way (see below).


user id and processes
-----------------------

* :func:`os.getuid` returns the current process's user id. 
* :func:`os.getgid` returns the current process's group id.
* :func:`os.geteuid` and  :func:`os.getegid` returns the effective user id and effective group id
* :func:`os.getpid` returns the current process id
* :func:`os.getppid` returns the parent's process id

Cross platform os attributes
===============================


An alternative character used by the OS to separate pathame components is provided by :func:`os.altsep`.

The :func:`os.curdir` refers to the current directory. **.** for unix and windows and **:** for Mac OS.

Another multi-platform function that could be useful is the line separator. Indeed the final character that ends a line is coded differently under Linux, Windows and MAC. For instance under Linux, it is the \n character but you may have \r or \r\n. Using the :func:`os.linesep` guarantees to use a universal line_ending character.  

The os.uname gives more information about your system::

    >>> os.uname
    ('Linux',
    'localhost.localdomain',
    '3.3.4-5.fc17.x86_64',
    '#1 SMP Mon May 7 17:29:34 UTC 2012',
    'x86_64')


The function :func:`os.name` returns the OS-dependent module (e.g., posix, doc, mac,...) 

The function :func:`os.pardir` refers to the parent directory (.. for unix and windows and :: for Mac OS).

The :func:`os.pathsep` function (also found in :func:`os.path.sep`) returns the correct path separator for your system (slash / under Linux and backslash \ under Windows). 

Finally, the :func:`os.sep` is the character that separates pathname components (/ for Unix, \ for windows and : for Mac OS). It is also available in :func:`os.path.sep` 

    >>> # under linux
    >>> os.path.sep
    '/'     

Another function that is related to multi-platform situations is the :func:`os.path.normcase` that 
is useful under Windows where the OS ignore cases. So, to compare two filenames you will need this function.

.. index:: getsize, curdir, isdir, isfile, islink, exists, getmtime, getatime

More about directories and files
-----------------------------------
:mod:`os.path` provides methods to extract information about path and file names::

    >>> os.path.curdir # returns the current directory ('.')
    >>> os.path.isdir(dir) # returns True if dir exists
    >>> os.path.isfile(file) # returns True if file exists
    >>> os.path.islink(link) # returns True if link exists
    >>> os.path.exists(dir) # returns True if dir exists (full pathname or filename)
    >>> os.path.getsize(filename) # returns size of a file without opening it.


You can access to the time when a file was last modified. Nevertheless, the output is not friendly user. Under Unix it corresponds to the time since the Jan 1, 1970 (GMT) and under Mac OS since Jan 1, 1904 (GMT)Use the time module
to make it easier to read::

    >>> import time
    >>> mtime = os.path.getmtime(filename) # returns time when the file was last modified

The output is not really meaningful since it is expressed in seconds. You can use the :mod:`time` module to get a better layout of that time::

    >>> print time.ctime(mtime)
    Tue Jan 01 02:02:02 2000

Similarly, the function :func:`os.path.getatime` returns  the last access time of a file and :func:`os.path.getctime` the metadata change time of a file.


Finally, you can get a all set of information using :func:`os.stat` such as file's size, access time and so on. The :func:`~os.stat` returns a tuple of numbers, which give you information about a file (or directory).

.. doctest::
    :options: +skip

    >>> import stat
    >>> import time
    >>> def dump(st):
    ...    mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = st
    ...    print "- size:", size, "bytes"
    ...    print "- owner:", uid, gid
    ...    print "- created:", time.ctime(ctime)
    ...    print "- last accessed:", time.ctime(atime)
    ...    print "- last modified:", time.ctime(mtime)
    ...    print "- mode:", oct(mode)
    ...    print "- inode/dev:", ino, dev
    >>> dump(os.stat("todo.txt"))
    - size: 0 bytes
    - owner: 1000 1000
    - created: Wed Dec 19 19:40:02 2012
    - last accessed: Wed Dec 19 19:40:02 2012
    - last modified: Wed Dec 19 19:40:02 2012
    - mode: 0100664
    - inode/dev: 23855323 64770

There are other similar function :func:`os.lstat` for symbolic links, :func:`os.fstat` for file descriptor

You can determine is a path is a mount point using :func:`os.ismount`. Under unix, it checks if a path or file is mounted on an other device (e.g. an external hard disk).

.. see also:: http://effbot.org/librarybook/os.htm

.. index:: splitdrives, splitext, abspath,dirname, basename

Splitting paths
---------------------

To get the base name of a path (last component)::


    >>> import os
    >>> os.path.basename("/home/user/temp.txt")
    temp.txt

To get the directory name of a path, use :func:`os.path.dirname`::

    >>> import os
    >>> os.path.dirname("/home/user/temp.txt")
    /home/user

The :func:`os.path.abspath` returns the absolute path of a file::


    >>> import os
    >>> os.path.abspath('temp.txt')


In summary, consider a file *temp.txt* in */home/user*:

========== ======================
function   Output
========== ======================
basename   'temp.txt'
dirname     '' 
split      ('', 'temp.txt')
splitdrive ('', 'temp.txt')
splitext   ('temp'; 'txt')
abspath    '/home/user/temp.txt
========== ======================
    

::

    os.path.extsep       os.path.genericpath  os.path.realpath
    os.path.relpath      os.path.samefile
    os.path.sameopenfile os.path.samestat          
    os.path.isab         
    os.path.commonprefix 
    os.path.defpath      os.path.supports_unicode_filenames
    os.path.devnull      os.path.lexists 
    os.path.warnings     .expanduser       os.path.expandvars  

Split the basename and directory name in one function call using :func:`os.path.split`. The ``split`` function only splits off the last part of a component. In order to split off all parts, you need to write your own function:

.. note:: the path should not end with '/', otherwise the name is empty.

    os.path.split('/home/user') is not the same as  os.path.split('/home/user/')


.. doctest::

    >>> def split_all(path):
    ...    parent, name = os.path.split(path)
    ...    if name == '':
    ...        return (parent, )
    ...    else:
    ...        return split_all(parent) + (name,)
    >>> split_all('/home/user/Work')
    ('/', 'home', 'user', 'Work')


The :func:`os.path.splitext` function splits off the extension of a file::

    >>> os.path.splitext('image.png')
    ('image', 'png')

For windows users, you can use the :func:`os.splitdrive` that returns a tuple with 2 strings, there first one being the drive.

Conversely, the ``join`` method allows to join several directory name to create a full path name:

.. doctest::

    >>> os.path.join('/home', 'user')
    '/home/user'


:func:`os.path.walk` scan a directory recursively and apply a function of each item found (see also :func:`os.walk` above)::

    def print_info(arg, dir, files):
        for file in files:
            print dir + '    ' + file
    os.path.walk('.', print_info, 0)


Accessing environment variables
===================================

You can easily acecss to the environmental variables::

    import os
    os.environ.keys()

and if you know what you are doing, you can add or replace a variable::

    os.environ[NAME] = VALUE


sys module
=============

When starting a Python shell, Python provides 3 file objects called stadnard input, stadn output and standard error.
There are accessible via the sys module::

    sys.stderr
    sys.stdin
    sys.stdout



The :attr:`sys.argv` is used to retrieve user argument when your module is executable.

 
Another useful attribute in the :attr:`sys.path` that tells you where Python is searching for modules on your system. see :ref:`docmodule` for more details.


Information
---------------

* sys.platform returns the platform version (e.g., linux2)
* sys.version returns the python version
* sys.version_info returns a named tuple


::

        sys.exitfunc               sys.last_value             sys.pydebug
        sys.flags                  sys.long_info              sys.real_prefix
        sys.builtin_module_names   sys.float_info             sys.setcheckinterval
        sys.byteorder              sys.float_repr_style       sys.maxsize                sys.setdlopenflags
        sys.call_tracing           sys.getcheckinterval       sys.maxunicode             sys.setprofile
        sys.callstats              sys.meta_path             sys.copyright     
        sys.getdlopenflags         sys.modules                sys.settrace
        sys.displayhook            sys.getfilesystemencoding  sys.path                   
        sys.dont_write_bytecode    sys.getprofile             sys.path_hooks             
        sys.exc_clear              sys.path_importer_cache   
        sys.exc_info               sys.getrefcount              sys.exc_type               sys.getsizeof              sys.prefix                 sys.excepthook             
        sys.gettrace           sys.ps1                 
        sys.exec_prefix     sys.ps2                    sys.warnoptions
        sys.executable             sys.last_traceback         sys.ps3     
        sys.last_type              sys.py3kwarning            



The sys.modules attribute returns list of all the modules that have been imported so far in your environment.

recursion
-----------

See the :ref:`functions` section to know more about recursions. You can limit the number of recursions and know about the number itself using the :func:`sys.getrecursionlimit` and :func:`sys.setrecursionlimit` functions.





UserDict module
=================




:References: [Norton]_



