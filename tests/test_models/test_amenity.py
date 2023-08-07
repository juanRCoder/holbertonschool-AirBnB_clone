#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_amenity_name_is_none(self):
        obj_amenity = Amenity()
        self.assertIsNone(obj_amenity.name, "name is not None")
