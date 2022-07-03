#!/usr/bin/python3
"""
Unit tests State class
"""
from models.state import State
import unittest
from datetime import datetime


class TestState(unittest.TestCase):
    """
    Unit tests State class
    """

    def setUp(self):
        """
        Initialization
        """
        self.state_1 = State()
        self.state_1.name = "Florida"
        self.state_2 = State()

    def test_base_attribute(self):
        """
        Test attribute BaseModel
        """
        self.assertIsNotNone(self.state_1.id)
        self.assertIsNotNone(self.state_1.created_at)
        self.assertIsNotNone(self.state_1.updated_at)

    def test_base_type(self):
        """
        Test type attribute BaseModel
        """
        self.assertEqual(type(self.state_1.id), str)
        self.assertEqual(type(self.state_1.created_at), datetime)
        self.assertEqual(type(self.state_1.updated_at), datetime)

    def test_state_attribute(self):
        """
        Test attribute State class
        """
        self.assertEqual(self.state_1.name, "Florida")

    def test_no_arg(self):
        """
        Test State class with no attributes
        """
        self.assertEqual(self.state_2.name, "")

    def test_state_type(self):
        """
        Test type attribute State class
        """
        self.assertEqual(type(self.state_1.name), str)
        self.assertEqual(type(self.state_2.name), str)


if __name__ == '__main__':
    unittest.main()
