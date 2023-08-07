#!/usr/bin/python3
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def Test_city_name_is_none(self):
        city = City(name=None)
        self.assertIsNone(city.name, "name is not None")

    def test_city_state_id_is_none(self):
        city = City(state_id=None)
        self.assertIsNone(city.state_id, "State_id is not None")


if __name__ == '__main__':
    unittest.main()
