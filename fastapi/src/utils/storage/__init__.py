from fastapi import UploadFile
from src.config.app.config import settings_app
import random
import string
import shutil
import imghdr  # Import the imghdr module
import base64

class Storage:
    def save(self, file: UploadFile, disk: str):
        file_ext = file.filename.split('.')[-1]
        filename = self.get_filename(file_ext)
        path_to_save = self.get_path(disk, filename)

        with open(path_to_save, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return filename

    def save_from_base64(self, image: str, disk: str):
        file_data = base64.b64decode(image)
        file_ext = imghdr.what(None, h=file_data)
        filename = self.get_filename(file_ext)
        path_to_save = self.get_path(disk, filename)

        with open(path_to_save, "wb") as f:
            f.write(file_data)

        return filename

    def get_path(self, disk, file_name):
        return settings_app.APP_PATH + '/storage/' + disk + '/' + file_name

    def get_filename(self, file_ext: str):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(30)) + '.' + file_ext