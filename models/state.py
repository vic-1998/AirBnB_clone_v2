#!/usr/bin/python3
'''define class state'''
from models.base_model import BaseModel


class State(BaseModel):
    '''class state'''

    name = ""

    def __init__(self, *args, **kwargs):
        '''constructor method'''
        super().__init__(*args, **kwargs)
