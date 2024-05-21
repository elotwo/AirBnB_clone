#!/usr/bin/python3
"""
the class Basemodel set a uniq id, name, created time and as well the time it was updated
"""
import uuid
from datetime import datetime
import json

class BaseModel:
    """
    class Basemodel
    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            self.id = str(uuid.uuid4())
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        value = datetime.strptime(value,"%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.my_number = 0
            self.name = ''
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ the string function prints all BaseModel atrribute in strings """
        return f"[{self.__class__.__name__}]({(self.id)}) {self.__dict__}"
    def save(self):
        """ function save the updated time """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        this function convert object to dictionary
        """
        dict_repr = self.__dict__.copy()
        dict_repr["__class__"] = self.__class__.__name__
        dict_repr["created_at"] = self.created_at.isoformat()
        dict_repr["updated_at"] = self.updated_at.isoformat()
        return dict_repr


