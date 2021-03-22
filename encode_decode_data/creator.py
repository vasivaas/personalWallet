class Creator:
    def __init__(self):
        self._objects = {}

    def register(self, specific_type: str, specific_object: object) -> None:
        self._objects[specific_type] = specific_object

    def create(self, specific_type: str) -> object:
        current_object = self._objects.get(specific_type)
        if current_object is None:
            raise ValueError(specific_type)
        else:
            return current_object
