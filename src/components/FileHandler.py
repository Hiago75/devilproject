import shutil
from os.path import join, abspath, exists


class FileHandler:
    def __init__(self, ) -> None:
        self.assets_folder = self.get_assets_dir()

    def get_assets_dir(self):
        src_dir = abspath(f'{abspath(__file__)}/../..')
        assets_dir = join(src_dir, 'assets')

        return assets_dir

    def copy_asset_file(self, filename: str, project_directory: str):
        final_dir = join(project_directory, filename + '.sample')
        shutil.copyfile(join(
            self.assets_folder, filename), final_dir)

        return final_dir

    def create_file(self, filepath):
        if exists(filepath):
            return

        config_file = open(filepath, 'x')
        config_file.close()
