#!/usr/bin/python
"""Contains class State"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """The Amenity class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
