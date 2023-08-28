#!/usr/bin/python3


def safe_print_integer(value):
    """prints an integer with "{:d}".format()

    Arguments:
        value (int): the int to be printed

    Returns:
        if TypeErrors or ValueErrors occur - False, Otherwise - True
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
