#!/usr/bin/python3
"""defines object attribute lookup"""


def lookup(obj):
    """return list of object's available attribute"""
    return (dir(obj))
