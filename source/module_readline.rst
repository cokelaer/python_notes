readline
================


In ipython; there is a nice tab completion available among other nice features. How does that work ?
::

    import readline
    except ImportError:
        print "Unable to load readline module."
    else:
        import rlcompleter
        readline.parse_and_bind("tab: complete")

::

    >>> class myclass:
    ...    def function(self):
    ...       print "my function"
    ... 
    >>> class_instance = myclass()
    >>> class_instance.<TAB>
    class_instance.__class__   class_instance.__module__
    class_instance.__doc__     class_instance.function
    >>> class_instance.f<TAB>unction()
