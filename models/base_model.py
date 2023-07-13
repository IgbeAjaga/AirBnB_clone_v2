#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
# import models

"""
Parent class to all classes in the AirBnB clone project
"""


class BaseModel():
    """Parent class for AirBnB clone project
    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        __save(self)
        __repr__(self)
        to_dict(self)
    """

    def __init__(self, **kwargs):
        """
        Initialize attributes: uuid4, dates when class was created/updated
        """
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    @classmethod
    def create(cls):
        obj = cls()
        # obj.id = str(uuid4())
        # obj.created_at = datetime.now()
        # obj.updated_at = datetime.now()
        # models.storage.new(obj)
        return obj

    # def __str__(self):
    #     """
    #     Return class name, id, and the dictionary
    #     """
    #     return ('[{}] ({}) {}'.
    #             format(self.__class__.__name__, self.id, self.__dict__))

    # def __repr__(self):
    #     """
    #     returns string repr
    #     """
    #     return (self.__str__())

    # def save(self):
    #     """
    #     Instance method to:
    #     - update current datetime
    #     - invoke save() function &
    #     - save to serialized file
    #     """
    #     self.updated_at = datetime.now()
    #     models.storage.save()

    def to_dict(self):
        """
        Return dictionary of BaseModel with string formats of times
        """
        return {
            "hello": 2
        }
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        return dic

            
def deserialize_json(json_obj):
    date_format = '%Y-%m-%dT%H:%M:%S.%f'
    if "created_at" == key:
        self.created_at = datetime.strptime(kwargs["created_at"],
                                            date_format)
    elif "updated_at" == key:
        self.updated_at = datetime.strptime(kwargs["updated_at"],
                                            date_format)
    elif "__class__" == key:
        pass


def get_model_class(object_type: str) -> BaseModel:
    print("subclases", BaseModel.__subclasses__())
    print("subclases names", [x.__name__ for x in BaseModel.__subclasses__()])
    return next((subclass for subclass in BaseModel.__subclasses__()
                if subclass.__name__ == object_type), None)
