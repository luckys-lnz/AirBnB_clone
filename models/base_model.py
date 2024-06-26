#!/usr/bin/python3
"""
defines all common attributes/methods
for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Defines common attributes and
    methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance.
        @params:
            *args(any): unused arguments
            **kwargs(dict): key/value Attribute name
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            from .__init__ import storage
            storage.new(self)

    def __str__(self):
        """
        Return a string representation of
        the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update the public instance attribute updated_at
        with the current datetime.
        """
        self.updated_at = datetime.now()
        from .__init__ import storage
        storage.save()

    def to_dict(self):
        """
        Return a dictionary containing all keys/values
        of __dict__ of the instance.
        """
        dict_rep = self.__dict__.copy()
        dict_rep['__class__'] = self.__class__.__name__
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()
        return dict_rep
