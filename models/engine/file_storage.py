#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine.
    Attributes:
        __file_path (str): The name of the
            file to save objects to.
        __objects (dict): A dictionary of
             instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """
        Set in __objects obj with key
        <obj_class_name>.id
        """
        obj_class = obj.__class__.__name__
        FileStorage.__objects[
            "{}.{}".format(obj_class, obj.id)] = obj

    def save(self):
        """
        Serialize __objects to the JSON file __file_path.
        """
        dict_obj = FileStorage.__objects
        objdict = {obj: dict_obj[obj].to_dict()
                   for obj in dict_obj.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(objdict, file)

    def reload(self):
        """
        Deserialize the JSON file __file_path
        to __objects, if it exists.
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.loads(f.read())
                from models.base_model import BaseModel
                from models.user import User
                for key, value in obj_dict.items():
                    if value['__class__'] == 'BaseModel':
                        FileStorage.__objects[key] = BaseModel(**value)
                    elif value['__class__'] == 'User':
                        FileStorage.__objects[key] = User(**value)
                    elif value['__class__'] == 'Place':
                        FileStorage.__objects[key] = Place(**value)
                    elif value['__class__'] == 'State':
                        FileStorage.__objects[key] = State(**value)
                    elif value['__class__'] == 'City':
                        FileStorage.__objects[key] = City(**value)
                    elif value['__class__'] == 'Amenity':
                        FileStorage.__objects[key] = Amenity(**value)
                    elif value['__class__'] == 'Review':
                        FileStorage.__objects[key] = Review(**value)

        except FileNotFoundError:
            pass

