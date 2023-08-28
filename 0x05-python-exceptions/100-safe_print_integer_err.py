#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """prints an integer with "{:d}".format()

    if a ValueError message is found, a corresponding
    message is printed to stderr

    Arguments:
        value: (int) the integer to print

    Returns:
        if a TypeError or ValueError occurs - False, Otherwise - True
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
