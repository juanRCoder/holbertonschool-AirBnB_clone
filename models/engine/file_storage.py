#!/usr/bin/python3
""" This module hast tha class FileStorage """
import json
import os
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


class FileStorage:
    """this is a class filestorgare"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """this a method all"""
        return FileStorage.__objects

    def new(self, obj):
        """this a method new that generate a new isntance"""
        key = f"{obj.__class__.__name__}.{obj.id}"

        self.__objects[key] = obj

    def save(self):
        """this method serealized the dictionary in JSON"""
        dictionary = {}

        for k, v in self.__objects.items():
            dictionary[k] = v.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(dictionary, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists"""
        from models.base_model import BaseModel
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                data = f.read()
                JSON_dict = json.loads(data)

                for key, value in JSON_dict.items():
                    value = JSON_dict[key]
                    obj = eval(value['__class__'])(**value)
                    FileStorage.__objects[key] = obj
        else:
            pass
