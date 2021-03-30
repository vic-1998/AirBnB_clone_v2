#!/usr/bin/python3
"""
Contains Class City
"""

from models.base_model import BaseModel


class City(BaseModel):
    """The City class"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of the City Class"""
        super().__init__(*args, **kwargs)
