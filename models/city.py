#!/usr/bin/python3
'''define class city'''
from models.base_model import BaseModel


class City(BaseModel):
    '''class City'''
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        '''constructor method'''
        super().__init__(*args, **kwargs)
