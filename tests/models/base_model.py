#!/usr/bin/python3
import uuid
from datetime import datetime
class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)
                if 'id' not in kwargs:
                    self.id = str(uuid.uuid4())
                if 'created_at' not in kwargs:
                    created_at = datetime.now()
                if 'updated_at'not in kwargs:
                    updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.my_number = 0
            self.name = ''
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
    def save(self):
        self.updated_at = datetime.now()
    def to_dict(self):
        dict_repr = self.__dict__.copy()
        dict_repr["__class__"] = self.__class__.__name__
        dict_repr["created_at"] = self.created_at.isoformat()
        dict_repr["updated_at"] = self.updated_at.isoformat()
        return dict_repr
    def to_json_string(self):
        return json.dumps(self.to_dict(), indent=4)
    def __str__(self):
        return f"[BaseModel]({self.id}, 'name': {self.name}, 'my_number': {self.my_number}, 'updated_at': {self.updated_at}, 'created_at': {self.created_at})"
    def __repr__(self):
        return f"[BaseModel]({self.id}, 'name': {self.name}, 'my_number': {self.my_number}, 'updated_at': {self.updated}, 'created_at': {self.created_at})"
