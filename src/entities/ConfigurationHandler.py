import os
import click

from configparser import ConfigParser
from src.components.ArgumentChecker import ArgumentChecker

from src.components.FileHandler import FileHandler
from src.components.PromptHandler import PromptHandler


class ConfigurationHandler(FileHandler):
    def __init__(self) -> None:
        FileHandler.__init__(self)
        self.config_file_path = os.path.join(
            self.assets_folder, 'config.ini')
        self.prompt_handler = PromptHandler()
        self.argument_checker = ArgumentChecker()
        self.config_parser = ConfigParser()

        self.devilbox_root = None
        self.database_files_root = None
        self.database_user = None
        self.database_password = ''

    def promptOptions(self):
        # Roots
        self.devilbox_root = self.prompt_handler.create_text_prompt(
            'Diretório raiz do devilbox (caminho completo)', self.argument_checker.verify_directory)

        self.database_files_root = self.prompt_handler.create_text_prompt(
            'Diretório dos arquivos de dump do MySQL (caminho completo)', self.argument_checker.verify_directory)

        # Credentials
        self.database_user = self.prompt_handler.create_text_prompt(
            'Usuário do MySQL usado no Devilbox')

        database_have_password = click.confirm(
            'O usuário MySQL tem senha?', default=True)

        if database_have_password:
            self.database_password = self.prompt_handler.create_text_prompt(
                'Senha para o usuário do MySQL')

    def create_section(self, section_name: str):
        self.config_parser.add_section(section=section_name)

    def create_option(self, section_name: str, option_name: str, option_value: str):
        self.config_parser.set(section_name, option_name, option_value)

    def create_printing_instructions(self):
        instructions = {
            'paths': {
                'devilbox_root': self.devilbox_root,
                'database_files_root': self.database_files_root,
            },
            'credentials': {
                'database_user': self.database_user,
                'database_password': self.database_password
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

    def read_field(self, section_name: str, option_name: str):
        self.config_parser.read(self.config_file_path)
        config = self.config_parser.get(section_name, option_name)

        if not config:
            return ''

        return config

    def run(self):
        self.promptOptions()

        click.clear()

        click.secho('Criando arquivo de configuração', fg="bright_blue")
        filepath = self.create_file(self.config_file_path)
        click.secho('Arquivo de configuração criado', fg="green")

        click.secho('-' * 50)

        click.secho('Inserindo configurações no arquivo', fg="bright_blue")
        self.config_parser.read(filepath)
        instructions = self.create_printing_instructions()
        self.create_fields_on_file(instructions)
        self.save_configuration(filepath)
        click.secho('Configurações inseridas no arquivo', fg="green")
