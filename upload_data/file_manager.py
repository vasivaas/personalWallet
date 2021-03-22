from pathlib import Path

dir_name = 'data_base'
file = 'data.json'
db_directory_path = f'{Path.cwd()}/{dir_name}'
db_file_path = db_directory_path + '/' + file

directory_path = Path(db_directory_path)
file_path = Path(db_file_path)


def check_db_file() -> None:
    if file_path.is_file():
        return
    else:
        _create_db_dir()
        _create_db_file()


def _create_db_dir() -> None:
    directory_path.mkdir(parents=False, exist_ok=False)


def _create_db_file() -> None:
    file_path.touch(exist_ok=False)
