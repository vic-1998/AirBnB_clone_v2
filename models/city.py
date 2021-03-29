#!/usr/bin/python3
""" City Module for HBNB project """
import models
from models.base_model import BaseModel
import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel):
    """ The city class, contains state ID and name """
    if models.storage_method == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('state.id'), nullable=False)
        name = Column(String(128), nullable=False)
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """Initializes city"""
        super().__init__(*args, **kwargs)
