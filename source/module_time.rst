.. _time_module:

The time module
##################################

The :mod:`time` module provide tools for, among other things, getting the current time, manipulating, formatting and reading times and dates. Dates can be represented as either a real number (the seconds since 0 hours, January 1 in the “epoch,” a platform-dependent year; for UNIX, it’s 1970), or a tuple containing nine integers. These integers are explained in the following table.

The tuple (2002, 1, 21, 12, 2, 56, 0, 21, 0) represents January 21, 2002, at 12:02:56, which is a Monday, and the 21st day of the year.

.. seealso:: These :mod:`datetime` modules.

Quick start
=============




ndex        Field                   Value
============ ======================= =====================================
0            Year                    For example, 2000, 2001, and so on
1            Month                   In the range 1Â­12
2            Day                     In the range 1Â­31
3            Hour                    In the range 0Â­23
4            Minute                  In the range 0Â­59
5            Second                  In the range 0Â­61
6            Weekday                 In the range 0Â­6, where Monday is 0
7            Julian day              In the range 1Â­366
8            Daylight Savings        0, 1, or Â­1
============ ======================= =====================================


Here are some functions.

========================== ==================================================
Function                   Description
========================== ==================================================
asctime([tuple])           Converts time tuple to a string
localtime([secs])          Converts seconds to a date tuple, local time
mktime(tuple)              Converts time tuple to local time
sleep(secs)                Sleeps (does nothing) for secs seconds
strptime(string[, format]) Parses a string into a time tuple
time()                     Current time (seconds since the epoch, UTC)
========================== ==================================================

    >>> import time
    >>> date1 = (2005, 1, 1, 0, 0, 0, -1, -1, -1)
    >>> time.asctime(date1)
    'Sun Jan  1 00:00:00 2005'



.. todo:: time.accept2dyear  time.ctime   time.struct_time   time.tzset
    time.altzone       time.daylight              
    time.gmtime        time.strftime      time.timezone      
    time.clock         time.tzname        

