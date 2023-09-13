#!/usr/bin/python3
"""define the class Student"""


class Student:
    """Represents student"""

    def __init__(self, first_name, last_name, age):
        """Initialise new Student

        Arguments:
            first_name - str: first name of the student
            last_name - str: last name of the student
            age - int: age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get dictionary representation of the Student"""
        return self.__dict__
