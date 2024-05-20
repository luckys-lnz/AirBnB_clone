#!/usr/bin/python3
"""
Defines the state model
"""
from .base_model import BaseModel


class City(BaseModel):
    """
        Definition of City objects
    """
    state_id = ""
    name = ""
