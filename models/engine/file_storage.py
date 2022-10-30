#!/usr/bin/python3
'''
    Represents a  FileStorage class
'''
import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    '''
    Class that serializes instances to a JSON file and deserializes
    JSON file to instances
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
        Method to return the dictionay __object
        '''
        return self.__objects

    def new(self, obj):
        '''
        set a new object with the obj in the key
        '''
        if obj:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        '''
        Method to serializes __objects to the JSON file
        '''
        dic_objects = {}
        for key, value in FileStorage.__objects.items():
            dic_objects[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w+') as f:
            json.dump(dic_objects, f)

    def reload(self):
        '''
        deserializes the JSON file to __objects
        '''
        try:
            with open(FileStorage.__file_path, 'r') as f:
                json_dict = json.load(f)
                for key, value in json_dict.items():
                    FileStorage.__objects[key] = eval(
                        value['__class__'] + '(**value)')
        except FileNotFoundError:
            pass
