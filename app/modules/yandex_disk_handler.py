import yadisk
from app import app
from io import BytesIO


def upload_to_yandex_disk(file: BytesIO, file_name: str):
    y = yadisk.YaDisk(token=app.config['YANDEX_TOKEN'])
    path_full_to = f"{app.config['YANDEX_KEY_FILES_PATH']}/{file_name}"
    print(path_full_to)
    y.upload(file, path_full_to, overwrite=True)

    return None
