from distutils.command.config import config
import click
import os

from src.components.FileHandler import FileHandler


class SetupChecker(FileHandler):
    def __init__(self) -> None:
        FileHandler.__init__(self)
        self.config_file_dir = os.path.join(self.assets_folder, 'config.ini')
        self.wp_config_file_dir = os.path.join(
            self.assets_folder, 'wp-config.php')

    def __check_config(self):
        config_exists = os.path.exists(self.config_file_dir)

        if not config_exists:
            raise click.BadArgumentUsage(
                'Opa, parece que você ainda não configurou o DevilProject. Para configurar ele rode o comando "devilproject config"')

    def __check_wp_config(self):
        wp_config_exists = os.path.exists(self.wp_config_file_dir)

        if not wp_config_exists:
            raise click.BadArgumentUsage(
                'O arquivo wp-config.php está ausente. Baixe ele pelo repositório do GitHub')

    def run(self):
        self.__check_config()
        self.__check_wp_config()
