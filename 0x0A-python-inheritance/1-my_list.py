#!/usr/bin/python3
"""define an inherited list class MyList"""


class MyList(list):
    """Execute sorted print for the built-in list class"""

    def print_sorted(self):
        """Prints list in the sorted's ascending order"""
        print(sorted(self))
