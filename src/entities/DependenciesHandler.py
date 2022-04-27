import subprocess
import os
from time import sleep

import click


class DependenciesHandler():
    def __init__(self, project_directory) -> None:
        self.project_directory = project_directory

    def check_files_exists(self):
        path_to_json = os.path.join(self.project_directory, 'composer.json')
        path_to_lock = os.path.join(self.project_directory, 'composer.lock')

        composer_json_exists = os.path.exists(path_to_json)
        composer_lock_exists = os.path.exists(path_to_lock)

        return composer_json_exists and composer_lock_exists

    def composer_install(self):
        os.chdir(self.project_directory)
        os.system('composer install')

    def run(self):
        files_exists = self.check_files_exists()

        if(files_exists):
            click.secho('Instalando as dependencias do composer',
                        fg="bright_blue")
            self.composer_install()
            click.secho('Dependencias instaladas', fg='green')
            sleep(2)
            click.clear()
