import os
import click

from src.components.FileHandler import FileHandler
from src.entities.ConfigurationHandler import ConfigurationHandler


class WordPressConfigHandler:
    def __init__(self, project_name, project_directory, configuration_handler) -> None:
        self.project_directory = project_directory
        self.project_name = project_name
        self.file_handler = FileHandler()
        self.configuration_handler = configuration_handler
        self.db_name, self.db_prefix, self.domain, self.db_user, self.db_password = self.get_config_data()

    def create_base_file(self):
        config_file_dir = self.file_handler.copy_asset_file(
            'wp-config.php', self.project_directory)

        return config_file_dir

    def get_config_data(self):
        db_name = click.prompt('Qual o nome do arquivo da base de dados?')
        db_prefix = click.prompt(
            'Qual o prefixo das tabelas da base de dados?')
        domain = self.project_name + '.loc'
        db_user = self.configuration_handler.read_field(
            'credentials', 'database_user')
        db_password = self.configuration_handler.read_field(
            'credentials', 'database_password')

        return db_name, db_prefix, domain, db_user, db_password

    def replace_statments(self, config_file_dir):
        new_config_dir = os.path.join(self.project_directory, 'wp-config.php')

        self.file_handler.replace_statments(config_file_dir, new_config_dir, statments={
            '<dbname>': self.db_name,
            '<prefix>': self.db_prefix,
            '<domain>': self.domain,
            '<dbuser>': self.db_user,
            '<dbpassword>': self.db_password,
        })

    def run(self):
        click.clear()
        click.secho(
            'Criando o arquivo de configuração do wordpress', fg="bright_blue")
        config_file_dir = self.create_base_file()
        self.replace_statments(config_file_dir)
        click.secho('Arquivo de configuração criado', fg="green")

        return self.db_name
