Threading
##########

Some definitions before starting:

* A **thread** is the smallest unit of code that can be executed. 
* A program that has more than one thread is **multithreaded**.
* A **process** is an executing instance of a program.
* A process as a complete set of data and variables while one or more threads may share the same data.

Note that for simple multiprocessing, you may also use the :mod:`os` module with :func:`fork` or :func:`spawn` function families (See the :ref:`os_module` page). However, the issue with *fork* is that it has to copy everything in the program to the new program and the system must have enough resources to handle that. Another issue with fork is that sometimes if several processes need to communicate, it may be difficult using multiple processes. In complex situation, the concept of thread is more appropriate.

The interest of threads is that there are multiplatform unlike subprocesses (unix only).

The thread module provides the functionalities for working with threads including locking, which is a synchronised mechanism. As we will see, only one thread can acquire a lock at a time. Before being too technical, let us start with a quick example.

Quick Start
===============

The :mod:`thread` module provides simple functionalities and higher level interface is provided within the :mod:`threading` module that should be used instead.

Let us start with the :mod:`thread` module though. It will give us some insights into threading. As a first example, let us run 2 functions in 2 different threads::

    >>> import thread
    >>> import time
    >>> def func1():
    ...    for i in range(0,3):
    ...        print("Inside func1")
    ...        time.sleep(2)
    >>> def func2():
    ...    for i in range(0,3):
    ...        print("Inside func2")
    ...        time.sleep(1)
    >>> thread.start_new_thread(func1, ())
    >>> thread.start_new_thread(func2, ())

    Inside func1
    Inside func2
    Inside func2
    Inside func2
    Inside func1
    Inside func1

The output shows that indeed the 2 threads are running at the same time: :func:`func2`, which is faster, ends up before the end :func:`func1`.

The function :func:`thread.start_new_thread` first argument is the function to call and its second argument is a tuple containing the positional list of arguments. Even though we have no arguments in this example, an empty tuple must be provided. Keyword arguments can also be provided. 


Locking
=========

The previous example is rather simple. The 2 threads run simultanously and do not need to communicate or wait for each other. 

Let us use now consider another example where you want to fetch several URLs and write the responses into a file, which is a **shared resource**. The main issue is that access to the file may be random or in the orst case occuring at the same time. To solve this issue, we need a **lock**. An instance of lock can be created as follows::

    lock = thread.allocate_lock()

Locks have 2 states: locked and unlocked. The state can be cheched with the :func:`thread.allocate_lock.locked` function::

    >>> lock.locked()
    False

2 additional methods are used to manipulate them: :meth:`thread.allocate_lock.acquire` and :meth:`thread.allocate_lock.release`. The rules linking the lock states and these functions are:

 * if the state is unlocked: a call to :func:`acquire` changes the state to locked.
 * if the state is locked: a call to :func:`acquire` blocks until another thread calls release().
 * if the state is unlocked: a call to :func:`release` raises a RuntimeError exception.
 * if the state is locked: a call to :func:`release` changes the state to unlocked().

.. note:: a lock is not owned by the thread that locked it; another thread may unlock it.

Here is now an example of multi threading with locking to fetch several URL and save the results in a file:: 

    import thread
    import time
    import urllib2

    # This function fetch the data from a URL
    def getData(url):
        try:
            f = urllib2.urlopen(url)
            data = f.read()
            f.close()
        except urllib2.URLError:
            data = "Not found. URLError"
        return data

    # This one tries to save the data from a URL into a file.
    # it is a common functionto shared resource (the file) and 
    # therefore requires a lock
    def fetchURL(url, filename, lock):
        data = getData(url)
        print("%s was requested and returned" % url)
        lock.acquire()
        try:
            f = open(filename, "a")
            f.write("Data from %s fetched\n" % url)
            f.close()
        finally:
            lock.release()
        return data

    lock = thread.allocate_lock()

    thread.start_new_thread(fetchURL, ("http://www.yahoo.fr","test.txt",lock))
    thread.start_new_thread(fetchURL, ("http://www.lemonde.fr","test.txt",lock))
    thread.start_new_thread(fetchURL, ("http://www.youtube.fr","test.txt",lock))

Re-Entrant locks
======================

The previous example shows how to use what is called **simple locking**. This does not work in all cases. consider a file that you want to read partially with a function that read the first part and another that reads the second part.
::

    def getPart1():
        lock.acquire()
        try:
            ... get first part of the data
        finally:
            lock.release()    

    def getPart2():
        lock.acquire()
        try:
            ... get first part of the data
        finally:
            lock.release()    

We use locking to mqke sure that the file is not changed while reading it. Now, the problem is that a function that reads both part is in trouble::

    def getAll():
        first = getPart1()
        second = getPart2()
        return first, second

Indeed, another thread may modify the file in between. A solution could be something like::

    def getAll():
        lock.acquire()
        try:
            first = getPart1()
            second = getPart2()
        except:
            lock.release()
        return first, second

However, the getAll function calls acquire so it blocks further acquire calls in getPart1 and 2. This can be soveld using flags but it starts to be complicated. A neat solution is provided in the threading module called RLock (for Re-Entrant locks) that we will start to use now. You would replace::


    lock = threading.Lock()
    lock.acquire()
    lock.acquire() # this blocks the lock

by::
    
    lock = threading.RLock()
    lock.acquire()
    lock.acquire() # this won't block !!


and the getAll() function above should take care of the recursive call to acquire/release functions.


Using the Threqding module
==============================

Let us revisit the previous examples with the :mod:`threading` module and its :class:`threading.Thread` class. The Thread class has a :meth:`run` method that needs to be defined by the user. Once set, you can call it using the start method. The example from the quick start section could be written::

    >>> import threading
    >>> import time
    >>> class ThreadExample(threading.Thread):
    >>>    def __init__(self, Id, dt):
    ...        super(ThreadExample, self).__init__()
    ...        self.id = Id
    ...        self.dt = dt
    >>>    def run(self):
    ...        for i in range(0,3):
    ...            print("Inside func %s" % self.id)
    ...            time.sleep(self.dt)
    >>> t1 = ThreadExample("1", 1)
    >>> t2 = ThreadExample("2", 2)
    >>> t1.start(); t2.start()
    Inside func 1
    Inside func 2
    Inside func 1
    Inside func 1
    Inside func 2
    Inside func 2












Semaphore
===============
You can use semaphore, which is  a more advanced lock mechanism that has an internal counter. It only blocks if more than a given number of threads have attempted to hold the semaphore. This allows multiple threads to access the same code section simultaneously::

    semaphore = threading.BoundedSemaphore()
    semaphore.acquire() # decrements the counter
    ... access the shared resource
    semaphore.release() # increments the counter

If the counter reaches zero when acquired, the acquiring thread will block. Semaphores are used to limit access to resource with limited capacity, such as a network connection or a database server. Just initialize the counter to the maximum number, and the semaphore implementation will take care of the rest::

    semaphore = threading.BoundedSemaphore(10)

Python’s threading module provides two semaphore implementations; the Semaphore class provides an unlimited semaphore which allows you to call release any number of times to increment the counter. To avoid simple programming errors, it’s usually better to use the BoundedSemaphore class, which considers it to be an error to call release more often than you’ve called acquire.



Synchronisation between threads
=====================================

Events
--------
In the threading module, you can also find a class :class:`threading.Event` that is a simple synchronization object. The event represents an internal flag, and threads can wait for the flag to be set or unset. A server thread can wait for the flag to be set::
  
    >>> e = threading.Event()
    >>> e.wait()

wile the client manipulates the event as follows::

    >>> e = threading.Event()
    >>> e.isSet()
    False
    >>> e.set()
    >>> e.isSet()
    True
    >>> e.clear()
    >>> e.isSet()
    False

If the flag is set, the wait method doesn’t do anything. If the flag is cleared, wait will block until it becomes set again. Any number of threads may wait for the same event.

Conditions
--------------

A condition is a more advanced version of the event object. It represents a state change in the application, and a thread can wait for a given condition, or signal that the condition has happened. First, you need a condition object::

    # represents the addition of an item to a resource
    condition = threading.Condition()

The producing thread needs to acquire the condition before it can notify the consumers that a new item is available::

    # producer thread
    ... generate item
    condition.acquire()
    ... add item to resource
    condition.notify() # signal that a new item is available
    condition.release()

The consumers must acquire the condition (and thus the related lock), and can then attempt to fetch items from the resource::

    # consumer thread
    condition.acquire()
    while True:
        ... get item from resource
        if item:
            break
        condition.wait() # sleep until item becomes available
    condition.release()
    ... process item

The wait method releases the lock, blocks the current thread until another thread calls notify or notifyAll on the same condition, and then reacquires the lock. If multiple threads are waiting, the notify method only wakes up one of the threads, while notifyAll always wakes them all up.

To avoid blocking in wait, you can pass in a timeout value, as a floating-point value in seconds. If given, the method will return after the given time, even if notify hasn’t been called. If you use a timeout, you must inspect the resource to see if something actually happened.

Note that the condition object is associated with a lock, and that lock must be held before you can access the condition. Likewise, the condition lock must be released when you’re done accessing the condition. In production code, you should use try-finally or with, as shown earlier.

To associate the condition with an existing lock, pass the lock to the Condition constructor. This is also useful if you want to use several conditions for a single resource::

    lock = threading.RLock()
    condition_1 = threading.Condition(lock)
    condition_2 = threading.Condition(lock)



















.. seealso:: mod:`Queue`

Another Threading module example
=======================================
   

The following example shows how to use lock and threading to fetch several URLs at the same time
::

    class FetchUrls(threading.Thread):
        def __init__(self, urls, output, lock):
            self.lock = lock
    
        def run(self):
            while self.urls:
                self.lock.acquire()
                print 'lock acquired by %s' % self.name
                self.output.write(d.read())
                print 'write done by %s' % self.name
                print 'lock released by %s' % self.name
                self.lock.release()

    def main():
        lock = threading.Lock()
        t1 = FetchUrls("http://www.yahoo.fr", f, lock)
        t2 = FetchUrls("http://www.youtube.fr", f, lock)



Threading
============

Here is another example from [Norton]_ that illustrates the usage of the :class:`threading.Thread` class::

    import math
    from threading import Thread
    import time

    class SquareRootCalculator(object):
        """This class spawns a separate thread to calculate a bunch of 
        roots, and checks in it once a second until it finishes."""
        def __init__(self, target):
            """Turn on the calculator thread and, while waiting for it 
            finish, periodically monitor its progress."""
            self.results = []
            counter = self.CalculatorThread(self, target)
            print "Turning on the calculator thread..."
            counter.start()

            while len(self.results) < target:
                print "%d square roots calculated so far." % len(self.results)
                time.sleep(1)
            print "Calculated %s square root(s); the last one is sqrt(%d)=%f" % \
                (target, len(self.results), self.results[-1])
        class CalculatorThread(Thread):
            """A separate thread which actually does the calculations."""
            def __init__(self, controller, target):
                 """Set up this thread, including making it a daemon thread
                 so that the script can end without waiting for this thread to
                 finish."""
                 Thread.__init__(self)
                 self.controller = controller
                 self.target = target
                 self.setDaemon(True)
            def run(self):
                 """Calculate square roots for all numbers between 1 and the target,
                 inclusive."""
                 for i in range(1, self.target+1):
                     self.controller.results.append(math.sqrt(i))
    if __name__ == '__main__':
        import sys
        limit = None
        if len(sys.argv) > 1:
            limit = sys.argv[1]
            try:
                limit = int(limit)
            except ValueError:
                print "Usage: %s [number of square roots to calculate]" \
                   % sys.argv[0]
        SquareRootCalculator(limit)

Others
========

The threading.Thread class has some attributes htat can be useful. Each thread has a name attribute. It can be retrieved with :name: and be be set with the function :meth:`threading.Thread.setName`. 

You can check is a thread is alive::

    t.is_alive()
    t.isAlive()

You can check if the thread is a Daemon. 
::

    t.isDaemon()
    t.daemon()

or set it with setDaemon

threading
---------------

      threading.Timer


Thread class
--------------

        t.ident 
        t.join       
        


:References: 
        * http://www.laurentluce.com/posts/python-threads-synchronization-locks-rlocks-semaphores-conditions-events-and-queues/
        * http://www.artfulcode.net/articles/multi-threading-python/
