from typing import List

from patterns import singleton_meta as singleton
from encode_decode_data import constants
from encode_decode_data.creator import Creator as DeserializerCreator
from encode_decode_data.decode.deserializers import JsonDeserializer

deserializer_creator = DeserializerCreator()
deserializer_creator.register(specific_type=constants.json_format, specific_object=JsonDeserializer)


class ObjectDeserializer(metaclass=singleton.SingletonMeta):
    _creator = deserializer_creator

    def decode_data(self, serializer_format: str, encoded_data: object) -> List[object]:
        deserializer = self._creator.create(specific_type=serializer_format)
        return deserializer().str_to_object(encoded_data)
