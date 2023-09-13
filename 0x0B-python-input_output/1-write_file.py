#!/usr/bin/python3
"""defines file-writing operation functions"""


def write_file(filename="", text=""):
    """Writes string to UTF8 text file

    Arguments:
        filename - str: name of file to write
        text (str): text to write the file
    Returns:
        number of char written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
