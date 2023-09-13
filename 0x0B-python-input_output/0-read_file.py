#!/usr/bin/python3
"""defines text file-reading operation"""


def read_file(filename=""):
    """prints contents of UTF8 text file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
