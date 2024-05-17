#!/usr/bin/python3
import uuid
from datetime import datetime
class BaseModel:
    def __init__(self, name='', my_number=0):
        self.id = str(uuid.uuid4())
        self.my_number = my_number
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    def set_id(self, id=None):
        if id is None:
            self.id = str(uuid.uuid4())
        else:
            self.id = id
    def set_name(self, name):
        self.name = name
    def set_my_number(self, my_number):
        self.my_number = my_number
    def set_created_at(self, created_at=None):
        if created_at is None:
            self.created_at = datetime.now()
        else:
            self.created_at = created_at
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_my_number(self):
        return self.my_number
    def get_created_at(self):
        return self.created_at
    def get_updated_at(self):
        return self.updated_at
    def set_updated_at(self):
        self.updated_at = datetime.now()
    def save(self):
        self.updated = datetime.now()
    def to_dict(self):
        dict_repr = self.__dict__.copy()
        dict_repr["__class__"] = self.__class__.__name__
        dict_repr["created_at"] = self.created_at.isoformat()
        dict_repr["updated_at"] = self.updated_at.isoformat()
        return dict_repr
    def __str__(self):
        return f"[BaseModel]({self.id}, 'name': {self.name}, 'my_number': {self.my_number}, 'updated_at': {self.updated_at}, 'created_at': {self.created_at})"
    def __repr__(self):
        return f"[BaseModel]({self.id}, 'name': {self.name}, 'my_number': {self.my_number}, 'updated_at': {self.updated}, 'created_at': {self.created_at})"
