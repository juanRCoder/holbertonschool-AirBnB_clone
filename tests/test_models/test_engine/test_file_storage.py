#!/USR/BIN/PYTHON3
""" this module has TestCase of the FileStorage """
import os
import json
import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def test_file_path_is_none(self):
        file_path = FileStorage.__file_path
        self.assertIsNotNone(file_path, "__file_path es None")

    def test_file_object_is_list(self):
        file_object = FileStorage.__file_object
        self.assertIsInstance(file_object, dict, "file_object is not dict")

    def test_all_method(self):
        obj = FileStorage()
        all_obj = obj.all()

        self.assertIsInstance(all_obj, dict)


if _name_ == '_main_':
    unittest.main()
