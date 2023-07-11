#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """This is a Test an orders list of integers."""
        orders = [1, 2, 3, 4]
        self.assertEqual(max_integer(orders), 4)

    def test_unordered_list(self):
        """This is a Test an unordered list of integers."""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_begginning(self):
        """This is a Test a list with a beginning max value."""
        maxix_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(maxix_at_beginning), 4)

    def test_empty_list(self):
        """This is a Test an none list."""
        none = []
        self.assertEqual(max_integer(none), None)

    def test_one_element_list(self):
        """This is a Test a list with a single element."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """This is a Test a list of floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """This is a Test a list of ints and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """This is a Test a string."""
        string = "Gilbert"
        self.assertEqual(max_integer(string), 't')

    def test_list_of_strings(self):
        """This is a Test a list of stringsd."""
        stringsd = ["Gilbert", "is", "my", "name"]
        self.assertEqual(max_integer(stringsd), "name")

    def test_empty_string(self):
        """This is a Test an none string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
