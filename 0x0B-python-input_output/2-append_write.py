#!/usr/bin/python3
"""defines file-appending operation functions"""


def append_write(filename="", text=""):
    """Append string to end of a UTF8 text file

    Arguments:
        filename - str: Name of file to append on
        text - str: string to append onto the file
    Returns:
        Number of chars ppended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
