#!/usr/bin/python3
"""
Contains Class BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """The User class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of the User Class"""
        super().__init__(*args, **kwargs)
