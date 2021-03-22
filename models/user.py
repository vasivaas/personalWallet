from encode_decode_data import constants


class User:
    def __init__(self, full_name, budget=None):
        self.full_name = full_name
        self.budget = budget

    def encode(self, serializer):
        serializer.initial_object(new_object=self, type_key=constants.decode_json_attribute)
        serializer.add_property(property_name='full_name', property_value=self.full_name)
        serializer.add_property(property_name='budget', property_value=self.budget)
