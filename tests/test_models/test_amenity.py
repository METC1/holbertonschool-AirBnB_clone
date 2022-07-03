#!/usr/bin/python3
"""
Unit tests Amenity class
"""
from models.amenity import Amenity
import unittest
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """
    Unit tests Amenity class
    """

    def setUp(self):
        """
        Initialization
        """
        self.am_1 = Amenity()
        self.am_1.name = "Fire pits"
        self.am_2 = Amenity()

    def test_base_attribute(self):
        """
        Test attribute BaseModel
        """
        self.assertIsNotNone(self.am_1.id)
        self.assertIsNotNone(self.am_1.created_at)
        self.assertIsNotNone(self.am_1.updated_at)

    def test_base_type(self):
        """
        Test type attribute BaseModel
        """
        self.assertEqual(type(self.am_1.id), str)
        self.assertEqual(type(self.am_1.created_at), datetime)
        self.assertEqual(type(self.am_1.updated_at), datetime)

    def test_amenity_attribute(self):
        """
        Test attribute class Amenity
        """
        self.assertEqual(self.am_1.name, "Fire pits")

    def test_no_arg(self):
        """
        Test Amenity class with no attribut
        """
        self.assertEqual(self.am_2.name, "")

    def test_amenity_type(self):
        """
        Test type attribute class Amenity
        """
        self.assertEqual(type(self.am_1.name), str)
        self.assertEqual(type(self.am_2.name), str)


if __name__ == '__main__':
    unittest.main()
