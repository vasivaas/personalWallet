from typing import List
from progress.bar import FillingSquaresBar, ShadyBar

from patterns import singleton_meta as singleton
from upload_data import file_manager
from encode_decode_data import constants
from encode_decode_data.encode.object_serializer import ObjectSerializer
from encode_decode_data.decode.object_deserializer import ObjectDeserializer


class Uploader(metaclass=singleton.SingletonMeta):
    _file_path = file_manager.file_path

    def load_data(self) -> List[object]:
        """
            Loaded all data with file and return their.
            If file empty or exist return empty list
        """
        file_manager.check_db_file()
        bar = ShadyBar('Load data', suffix='%(percent)d%%', max=1)
        if self._file_path.stat().st_size == 0:
            return []
        with self._file_path.open() as f:
            bar.next()
            return ObjectDeserializer().decode_data(constants.json_format, f)

    def save_data(self, data: List[object]) -> int:
        """
           Save prepared data to file
        """
        file_manager.check_db_file()
        bar = FillingSquaresBar('Save data', suffix='%(percent)d%%', max=1)
        with self._file_path.open(mode='w') as f:
            bar.next()
            f.write(ObjectSerializer().encode_object(constants.json_format, data))
        return 0
