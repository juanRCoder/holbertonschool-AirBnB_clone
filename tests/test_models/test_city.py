#!/usr/bin/python3
import unittest
from models.tmp_city import City


class TestCity(unittest.TestCase):

    def test_city_name_is_none(self):
        city = City()
        self.assertIsNone(city.name, "name is not None")

    def test_city_state_id_is_none(self):
        city = City()
        self.assertIsNone(city.state_id, "State_id is not None")


if __name__ == '__main__':
    unittest.main()
