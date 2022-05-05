from distutils.command.config import config
from multiprocessing.sharedctypes import Value
import sys
import click
import os

from src.components.FileHandler import FileHandler


class SetupChecker(FileHandler):
    def __init__(self) -> None:
        FileHandler.__init__(self)
        self.__config_file_dir = os.path.join(self.assets_folder, 'config.ini')
        self.__wp_config_file_dir = os.path.join(
            self.assets_folder, 'wp-config.php')

    def __check_config(self):
        config_exists = os.path.exists(self.__config_file_dir)

        if not config_exists:
            click.secho(
                'Parece que você ainda não configurou a CLI. Faça isso rodando o comando devilproject config', fg="red")
            sys.exit()

    def __check_wp_config(self):
        wp_config_exists = os.path.exists(self.__wp_config_file_dir)

        if not wp_config_exists:
            click.secho(
                'O arquivo wp-config.php está ausente. Baixe ele pelo repositório do GitHub', fg="red")
            sys.exit()

    def run(self):
        self.__check_config()
        self.__check_wp_config()
