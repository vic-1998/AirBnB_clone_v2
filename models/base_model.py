#!/usr/bin/python3
'''super class'''
import uuid
from datetime import datetime
import models

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    '''main class'''

    def __init__(self, *args, **kwargs):
        '''constructor method'''

        if len(kwargs):
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if hasattr(self, "created_at") and type(self.created_at)\
                        is str:
                    self.created_at = datetime.strptime(value, time)
                if hasattr(self, "updated_at") and type(self.updated_at)\
                        is str:
                    self.updated_at = datetime.strptime(value, time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        '''print formal representation of Base model isntance'''
        strout = '['
        strout += str(self.__class__.__name__) + '] ('
        strout += str(self.id) + ') ' + str(self.__dict__)
        return strout

    def save(self):
        '''update attribute with datetime'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        newdic = self.__dict__.copy()
        if "created_at" in newdic:
            newdic["created_at"] = newdic["created_at"].strftime(time)
        if "updated_at" in newdic:
            newdic["updated_at"] = newdic["updated_at"].strftime(time)
        newdic["__class__"] = self.__class__.__name__
        return newdic
