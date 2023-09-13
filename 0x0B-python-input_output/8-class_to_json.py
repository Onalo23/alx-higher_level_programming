#!/usr/bin/python3
"""defines a Python class-to-JSON"""


def class_to_json(obj):
    """Return  dictionary represntation of a simple data structure"""
    return obj.__dict__
