#!/usr/bin/python3
"""defines the class Student"""


class Student:
    """Represents student"""

    def __init__(self, first_name, last_name, age):
        """Initialise a new Student

        Arguments:
            first_name - str: first name of student
            last_name - str: last name of student
            age - int: age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets dictionary representation of Student

        If attrs is a list of strings, represent only attributes
        include in list

        Arguments:
            attrs - list: the optional attribute to represent
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
