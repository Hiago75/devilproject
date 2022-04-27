import shutil
from os.path import join, abspath


class FileHandler:
    def __init__(self, ) -> None:
        self.assets_folder = self.get_assets_dir()

    def get_assets_dir(self):
        src_dir = abspath(f'{abspath(__file__)}/../..')
        assets_dir = join(src_dir, 'assets')

        return assets_dir

    def copy_asset_file(self, filename: str, project_directory: str):
        shutil.copyfile(join(
            self.assets_folder, filename), join(project_directory, filename))
