#!/usr/bin/python3
"""class Base"""

import json


class Base:
    """Representation of a Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        list_dict = []
        if list_objs is not None:
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        dummy = cls(1, 1)
        if dummy is not None:
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        try:
            with open(cls.__name__ + '.json', 'r', encoding='utf-8') as f:
                json_data = f.read()
        except FileNotFoundError:
            return []
        list_dict = cls.from_json_string(json_data)
        list_instances = [cls.create(**d) for d in list_dict]
        return list_instances
