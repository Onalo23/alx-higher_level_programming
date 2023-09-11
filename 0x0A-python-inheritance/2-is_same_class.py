#!/usr/bin/python3
"""defines class-check"""


def is_same_class(obj, a_class):
    """Checks if object is exactly instance of a given class

    Arguments:
        obj : object to be checked
        a_class- type: Class to match type of obj
    Returns:
        True, If obj is exactly instance of a_class, False otherwise
    """
    if type(obj) == a_class:
        return True
    return False
