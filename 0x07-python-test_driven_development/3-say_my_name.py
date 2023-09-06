#!/usr/bin/python3
"""defines name-printing function"""


def say_my_name(first_name, last_name=""):
    """Prints name

    Arguments:
        first_name (str): first name to print
        last_name (str): last name to print
    Raises:
        TypeError: If any of first_name or last_name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
