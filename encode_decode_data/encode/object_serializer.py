from typing import List

from patterns import singleton_meta as singleton
from encode_decode_data import constants
from encode_decode_data.creator import Creator as SerializerCreator
from encode_decode_data.encode.serializers import JsonSerializer

serializer_creator = SerializerCreator()
serializer_creator.register(specific_type=constants.json_format, specific_object=JsonSerializer)


class ObjectSerializer(metaclass=singleton.SingletonMeta):
    _creator = serializer_creator

    def encode_object(self, serialize_format: str, data: List[object]) -> str:
        serializer = self._creator.create(specific_type=serialize_format)
        return serializer().object_to_str(data)
