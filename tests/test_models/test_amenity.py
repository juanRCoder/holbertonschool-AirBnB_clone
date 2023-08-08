#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_name(self):
        obj_amenity = Amenity()

        self.assertEqual(obj_amenity.name, "")
