import os
from time import sleep

import click


class DependenciesHandler():
    def __init__(self, file_handler):
        self.__file_handler = file_handler

    def composer_install(self, folder_dir):
        path_to_json = os.path.join(folder_dir, 'composer.json')
        path_to_lock = os.path.join(folder_dir, 'composer.lock')

        composer_json_exists = self.__file_handler.check_file_exists(
            path_to_json)
        composer_lock_exists = self.__file_handler.check_file_exists(
            path_to_lock)

        if not composer_lock_exists or not composer_json_exists:
            click.BadParameter('Arquivo do composer não foi encontrado')

        os.chdir(folder_dir)
        os.system('composer install')

    def yarn_install(self, folder_dir):
        path_to_json = os.path.join(folder_dir, 'package.json')
        path_to_lock = os.path.join(folder_dir, 'yarn.lock')

        node_json_exists = self.__file_handler.check_file_exists(
            path_to_json)
        node_lock_exists = self.__file_handler.check_file_exists(
            path_to_lock)

        if not node_json_exists and not node_lock_exists:
            click.BadParameter('Arquivo do NPM não foi encontrado')

        os.chdir(folder_dir)
        os.system('yarn install')
