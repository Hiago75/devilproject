import os
import click
from src.components.FileHandler import FileHandler


class WordPressConfigHandler:
    def __init__(self, project_name, project_directory) -> None:
        self.project_directory = project_directory
        self.project_name = project_name
        self.file_handler = FileHandler()
        self.db_name, self.db_prefix, self.domain = self.get_config_data()

    def create_base_file(self):
        config_file_dir = self.file_handler.copy_asset_file(
            'wp-config.php', self.project_directory)

        return config_file_dir

    def get_config_data(self):
        db_name = click.prompt('Qual o nome do arquivo da base de dados?')
        db_prefix = click.prompt(
            'Qual o prefixo das tabelas da base de dados?')
        domain = self.project_name + '.loc'

        return db_name, db_prefix, domain

    def replace_statments(self, config_file_dir):
        original_config = open(config_file_dir, 'rt')

        new_config_dir = os.path.join(self.project_directory, 'wp-config.php')
        new_config = open(new_config_dir, 'wt')

        statments_to_be_replaced = {
            '<dbname>': self.db_name,
            '<prefix>': self.db_prefix,
            '<domain>': self.domain,
        }

        for line in original_config:
            statment = [
                statment for statment in statments_to_be_replaced.keys() if str(statment) in line]

            if statment:
                new_config.write(line.replace(
                    statment[0], statments_to_be_replaced[statment[0]]))
                continue

            new_config.write(line)

        original_config.close()
        new_config.close()

        os.remove(config_file_dir)

    def run(self):
        click.clear()
        click.secho(
            'Criando o arquivo de configuração do wordpress', fg="bright_blue")
        config_file_dir = self.create_base_file()
        self.replace_statments(config_file_dir)
        click.secho('Arquivo de configuração criado', fg="green")
