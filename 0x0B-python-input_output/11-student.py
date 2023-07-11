#!/usr/bin/python3
"""A class Student."""


class Student:
    """Representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.
        Args:
            first_name (str): A first name of the student.
            last_name (str): A last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Getting a dictionary representation of the Student.
        If attrs is a list of strings, represents only those attributes
        included in the list.
        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {n: getattr(self, n) for n in attrs if hasattr(self, n)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all the attributes of the Student.
        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for n, m in json.items():
            setattr(self, n, m)
