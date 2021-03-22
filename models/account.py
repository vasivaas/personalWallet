from encode_decode_data import constants


class Account:
    def __init__(self, login, password, user):
        self.login = login
        self.password = password
        self.user = user

    def encode(self, serializer):
        serializer.initial_object(new_object=self, type_key=constants.decode_json_attribute)
        serializer.add_property(property_name='login', property_value=self.login)
        serializer.add_property(property_name='password', property_value=self.password)
        serializer.add_property(property_name='user', property_value=self.user)
