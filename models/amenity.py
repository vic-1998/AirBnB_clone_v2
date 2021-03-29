#!/usr/bin/python3
'''define class amenity'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''class amenity'''

    name = ""

    def __init__(self, *args, **kwargs):
        '''constructor method'''
        super().__init__(*args, **kwargs)
