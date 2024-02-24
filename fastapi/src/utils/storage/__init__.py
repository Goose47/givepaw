from fastapi import UploadFile
from src.config.app.config import settings_app
import random
import string
import shutil


class Storage:
    def save(self, file: UploadFile, disk: str):
        file_ext = file.filename.split('.')[-1]

        characters = string.ascii_letters + string.digits
        file_name = ''.join(random.choice(characters) for _ in range(30)) + '.' + file_ext

        path_to_save = self.get_path(disk, file_name)

        with open(path_to_save, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return file_name

    def get_path(self, disk, file_name):
        return settings_app.APP_PATH + '/storage/' + disk + '/' + file_name
