import json
from typing import List

from patterns import singleton_meta as singleton
from encode_decode_data import constants


class JsonSerializer(metaclass=singleton.SingletonMeta):
    def __init__(self):
        self._current_object = None

    def initial_object(self, new_object: object, type_key: str):
        self._current_object = {
            type_key: new_object.__class__.__name__
        }

    def add_property(self, property_name: str, property_value):
        self._current_object[property_name] = property_value

    def object_to_str(self, data: List[object]) -> str:
        return json.dumps(data, default=self._encode_object, indent=4)

    def _encode_object(self, object_to_encode):
        if hasattr(object_to_encode, constants.obj_encode_method):
            object_to_encode.encode(self)
            return self._current_object
        else:
            return json.JSONEncoder.default(json.JSONEncoder(), object_to_encode)
