#!/USR/BIN/PYTHON3
""" this module has TestCase of the FileStorage """
import os
import json
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def test_file_path_is_none(self):
        file_path = FileStorage.__file_path
        self.assertIsNotNone(file_path, "__file_path es None")

    def test_file_object_is_list(self):
        file_object = FileStorage.__file_object
        self.assertIsInstance(file_object, dict, "file_object is not dict")


if _name_ == '_main_':
    unittest.main()