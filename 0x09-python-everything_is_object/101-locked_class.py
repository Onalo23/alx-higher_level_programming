#!/usr/bin/python3
"""defines locked class"""


class LockedClass:
    """
    prevent user from instantiating a new LockedClass attribute
    but for attributes called 'first_name'
    """

    __slots__ = ["first_name"]
