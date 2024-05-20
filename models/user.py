#!/usr/bin/python3
"""
    Class User that inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
        Public Attributes that will use FileStorage in engine
        folder to manage serialization and deserialization of Users
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
