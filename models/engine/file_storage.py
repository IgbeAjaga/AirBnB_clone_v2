#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel

class FileStorage:
    """Represent a storage engine using a JSON file.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Return a dictionary of instantiated objects in __objects.

        Args:
            cls (class, optional): The class of objects to filter.

        Returns:
            dict: A dictionary of objects filtered by class type (or all objects).
        """
        if cls is not None:
            if isinstance(cls, str):
                cls = eval(cls)
            cls_dict = {}
            for key, obj in self.__objects.items():
                if isinstance(obj, cls):
                    cls_dict[key] = obj
            return cls_dict
        return self.__objects

    def new(self, obj):
        """Set obj in __objects with key <obj_class_name>.id.

        Args:
            obj (BaseModel): The object to be set in __objects.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
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
        """Delete obj from __objects, if it exists.

        Args:
            obj (BaseModel, optional): The object to be deleted.
        """
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects.pop(key, None)

    def close(self):
        """Call the reload method."""
        self.reload()
