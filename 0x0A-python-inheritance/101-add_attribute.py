#!/usr/bin/python3
"""define function that adds attribute to an object"""


def add_attribute(obj, att, value):
    """Adds new attribute to an object

    Arguments:
        obj : object to add attribute into
        att - str: name of attributes to add to an obj
        value : value of att
    Raises:
        TypeError: If attribute can not be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
