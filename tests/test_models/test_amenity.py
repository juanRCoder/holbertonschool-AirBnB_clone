#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def testAmenity(self):
        obj_amenity = Amenity.name
        self.assertIsNone(obj_amenity, "name is none")
