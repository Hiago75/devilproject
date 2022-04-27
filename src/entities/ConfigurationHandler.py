import os
import click

from configparser import ConfigParser

from src.components.FileHandler import FileHandler


class ConfigurationHandler(FileHandler):
    def __init__(self) -> None:
        FileHandler.__init__(self)
        self.config_file_path = os.path.join(
            self.assets_folder, 'config.ini')
        self.config_parser = ConfigParser()

    def create_section(self, section_name):
        self.config_parser.add_section(section=section_name)

    def create_option(self, section_name, option_name, option_value):
        self.config_parser.set(section_name, option_name, option_value)

    def create_printing_instructions(self, devilbox_root, database_user):
        instructions = {
            'paths': {
                'devilbox_root': devilbox_root,
            },
            'credentials': {
                'database_user': database_user,
            },
        }

        return instructions

    def create_fields_on_file(self, instructions):
        for section in instructions:
            self.create_section(str(section))
            for option in instructions[section]:
                self.create_option(str(section), str(
                    option), instructions[section][option])

    def save_configuration(self, filepath):
        with open(filepath, 'wt') as config_file:
            self.config_parser.write(config_file)

    def run(self, devilbox_root, database_user):
        click.secho('Criando arquivo de configuração', fg="bright_blue")
        filepath = self.create_file(self.config_file_path)
        click.secho('Arquivo de configuração criado', fg="green")

        click.secho('Inserindo configurações no arquivo', fg="bright_blue")
        self.config_parser.read(filepath)

        instructions = self.create_printing_instructions(
            devilbox_root, database_user)
        self.create_fields_on_file(instructions)

        self.save_configuration(filepath)
        click.secho('Configurações inseridas no arquivo', fg="green")
