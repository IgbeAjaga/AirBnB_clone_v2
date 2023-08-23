#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class FileStorage:
    """Represents the storage engine using a JSON file.

    Attributes:
        __file_path (str): The path to the JSON file for data storage.
        __objects (dict): A dictionary to store objects in memory.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Retrieve a dictionary of objects.

        Args:
            cls (class, optional): The class of objects to retrieve.

        Returns:
            dict: A dictionary of objects (or a specific class of objects).
        """
        if cls is not None:
            if isinstance(cls, str):
                cls = eval(cls)
            class_objects = {}
            for key, obj in self.__objects.items():
                if isinstance(obj, cls):
                    class_objects[key] = obj
            return class_objects
        return self.__objects

    def new(self, obj):
        """Add a new object to the storage dictionary.

        Args:
            obj (BaseModel): The object to be added to storage.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize the objects to the JSON file."""
        serialized_objs = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """Deserialize the JSON file to objects, if it exists."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(class_name)(**value))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete an object from the storage.

        Args:
            obj (BaseModel): The object to be deleted from storage.
        """
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects.pop(key, None)

    def close(self):
        """Calls the reload method to reload the JSON file."""
        self.reload()
