# decorator without for a function with arguments
def check_validity(f):
    """decorator without for a function with arguments

    :param f: function on which the decorator is applied

    """

    # this is the actual wrapping 
    def wrap(*args, **kargs):
        """The decorator accepts functon with arguments and optional arguments
        It return false kargs['l'] == args[0] i.e. when a division by zero 
        will be performed. Otherwise, it returns the function.

        """
        l = kargs.get('l', 0)
        if args[0] == l:
            return False
        return f(*args, **kargs)

    return wrap



@check_validity
def division(n, l=10.):
    """

    :param float n: 
    :param float l:

    return :math:`\\frac{100}{(n-l)}`
    """
    return 100./(n - l)
