#!/usr/bin/python3
'''define class user'''
from models.base_model import BaseModel


class User(BaseModel):
    '''Class user'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        '''constructor method'''
        super().__init__(*args, **kwargs)
