#!/usr/bin/python3
"""define a text file insertion"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a given string in a file

    Arguments:
        filename - str: File name
        search_string str: The string to be searched within file
        new_string str: String to insert
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
