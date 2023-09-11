#!/usr/bin/python3
"""defines inherited class-checker"""


def inherits_from(obj, a_class):
    """Checks if objects is inherited instance of a class

    Arguments:
        obj : object to be checked
        a_class- type: Class to put type of obj into
    Returns:
        True - if obj is inherited instance of a_class
        otherwise - False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
