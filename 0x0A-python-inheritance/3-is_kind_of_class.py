#!/usr/bin/python3
"""defines class and inherited class-checker"""


def is_kind_of_class(obj, a_class):
    """Checks if object is instance or inherited instance of a class

    Arguments:
        obj : object to be checked
        a_class- type: Class to match type of obj
    Returns:
        True If obj is an instance or inherited instance of a_class,
        if otherwise False
    """
    if isinstance(obj, a_class):
        return True
    return False
