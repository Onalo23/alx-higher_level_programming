#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Executes a function 

    Arguments:
        fct: The function to execute
        args: Arguments for fct.

    Returns:
        if an error occurs - None, Otherwise - the result of the call to fct
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
