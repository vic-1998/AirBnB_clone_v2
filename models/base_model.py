#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


if models.storage_method == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""
    if models.storage_method == "db":
        id = Column(String(60), nullable=False, primary_key=True)
        created_at = Column(DateTime(), nullable=False,
                            default=datetime.utcnow())
        updated_at = Column(DateTime(), nullable=False,
                            default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            upda = 'updated_at'
            crea = 'created_at'
            if k, v in kwargs.items():
                if 'id' not in kwargs:
                    self.id = str(uuid.uuid4)
                if k == upda or k == crea:
                    date = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                    kwargs[k] = date
                if upda not in kwargs.keys():
                    self.updated_at = datetime.now()
                if crea not in kwargs.keys():
                    self.created_at = datetime.now()
                self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        models.storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                           (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary.keys():
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """Function that delete instance"""
        from models import storage
        storage.deletele(self)
