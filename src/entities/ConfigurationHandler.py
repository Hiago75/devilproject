import os

from src.components.FileHandler import FileHandler


class ConfigurationHandler(FileHandler):
    def __init__(self) -> None:
        FileHandler.__init__(self)
        self.config_file_path = os.path.join(
            self.assets_folder, 'config.ini')

    def run(self, devilbox_root):
        self.create_file(self.config_file_path)
