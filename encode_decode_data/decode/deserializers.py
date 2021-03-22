import json
from typing import List

from patterns import singleton_meta as singleton
from encode_decode_data import constants
from encode_decode_data.creator import Creator as ModelsCreator
from models import account, user

models_creator = ModelsCreator()
models = [account.Account, user.User]
for model in models:
    models_creator.register(model.__name__, model)


class JsonDeserializer(metaclass=singleton.SingletonMeta):
    _models_creator = models_creator

    def str_to_object(self, file_object) -> List[object]:
        return json.load(file_object, object_hook=self._decode_object)

    def _decode_object(self, encoded_data):
        if not isinstance(encoded_data, dict):
            return encoded_data
        model_name = encoded_data.pop(constants.decode_json_attribute)
        model_class = self._models_creator.create(model_name)
        return model_class(**encoded_data)
