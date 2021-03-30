#!/usr/bin/python
"""Contains class State"""
from models.base_model import BaseModel


class State(BaseModel):
    """The state class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
