#!/usr/bin/python3
"""The class Student."""


class Student:
    """To Representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initializing new Student.
        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """To Getting a dictionary representation of the Student."""
        return self.__dict__
