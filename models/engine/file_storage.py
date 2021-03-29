#!usr/bin/python3
'''Define FileStorage class'''
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

atri = {"BaseModel": BaseModel, "User": User, "City": City, "State": State,
        "Amenity": Amenity, "Place": Place, "Review": Review}


class FileStorage():
    '''Serialized instances to Json and Json to Instances'''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' return dict'''
        return self.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj_class_name>.id'''
        if obj:
            self.__objects["{}.{}".format(
                str(type(obj).__name__), obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_ob = {}
        for key in self.__objects:
            json_ob[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_ob, f)

    def reload(self):
        """
        Public instance method to deserialize the JSON file
        to __objects only if file exists
        """
        try:
            with open(self.__file_path, encoding="UTF-8") as myfile:
                obj = json.load(myfile)
            for key, value in obj.items():
                name = atri[value["__class__"]](**value)
                self.__objects[key] = name
        except FileNotFoundError:
            pass
