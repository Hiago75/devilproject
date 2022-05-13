import os
import shutil
from os.path import join, abspath, exists

from click import BadParameter


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

    def move_file(self, actual_directory, move_to):
        file_exists = exists(actual_directory)

        if not file_exists:
            raise BadParameter('O seu arquivo não foi encontrado')

        shutil.move(actual_directory, move_to)

    def create_file(self, filepath):
        if exists(filepath):
            return filepath

        config_file = open(filepath, 'x')
        config_file.close()

        return filepath

    def check_file_exists(self, filepath):
        file_exists = os.path.exists(filepath)

        return file_exists

    def replace_statments(self, original_file_dir, new_file_dir, statments):
        original_file = open(original_file_dir, 'rt')
        new_config = open(new_file_dir, 'wt')

        for line in original_file:
            statment = [
                statment for statment in statments.keys() if str(statment) in line]

            if statment:
                new_config.write(line.replace(
                    statment[0], statments[statment[0]]))
                continue

            new_config.write(line)

        original_file.close()
        new_config.close()

        os.remove(original_file_dir)
