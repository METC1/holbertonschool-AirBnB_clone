#!/usr/bin/python3
"""
Unit tests City class
"""
from models.city import City
from models.state import State
import unittest
from datetime import datetime


class TestCity(unittest.TestCase):
    """
    Unit tests City class
    """

    def setUp(self):
        """
        Initialization
        """
        self.city_1 = City()
        self.city_1.name = "Orlando"
        self.state = State()
        self.state.name = "Florida"
        self.city_1.state_id = self.state.id
        self.city_2 = City()

    def test_base_attribute(self):
        """
        Test attribute BaseModel
        """
        self.assertIsNotNone(self.city_1.id)
        self.assertIsNotNone(self.city_1.created_at)
        self.assertIsNotNone(self.city_1.updated_at)

    def test_base_type(self):
        """
        Test type attribute BaseModel
        """
        self.assertEqual(type(self.city_1.id), str)
        self.assertEqual(type(self.city_1.created_at), datetime)
        self.assertEqual(type(self.city_1.updated_at), datetime)

    def test_city_attribute(self):
        """
        Test attribute City class
        """
        self.assertEqual(self.city_1.name, "Orlando")
        self.assertEqual(self.city_1.state_id, self.state.id)

    def test_no_arg(self):
        """
        Test City class with no attributes
        """
        self.assertEqual(self.city_2.name, "")

    def test_city_type(self):
        """
        Test type attribute City class
        """
        self.assertEqual(type(self.city_1.name), str)
        self.assertEqual(type(self.city_1.state_id), str)
        self.assertEqual(type(self.city_2.name), str)


if __name__ == '__main__':
    unittest.main()
