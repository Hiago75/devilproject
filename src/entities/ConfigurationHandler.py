import os
import click

from configparser import ConfigParser
from src.components.ArgumentChecker import ArgumentChecker

from src.components.FileHandler import FileHandler
from src.components.PromptHandler import PromptHandler


class ConfigurationHandler(FileHandler):
    def __init__(self, prompt_handler, argument_checker, config_parser) -> None:
        FileHandler.__init__(self)
        self.__config_file_path = os.path.join(
            self.assets_folder, 'config.ini')

        self.prompt_handler = prompt_handler
        self.argument_checker = argument_checker
        self.config_parser = config_parser

        self.__devilbox_root = None
        self.__database_files_root = None
        self.__database_user = None
        self.__projects_root = None
        self.__database_password = ''

    def __promptOptions(self):
        # Roots
        self.__devilbox_root = self.prompt_handler.create_text_prompt(
            'Diretório raiz do devilbox (caminho completo)', self.argument_checker.verify_directory)

        self.__projects_root = os.path.join(
            self.__devilbox_root, 'data', 'www')

        self.__database_files_root = self.prompt_handler.create_text_prompt(
            'Diretório dos arquivos de dump do MySQL (caminho completo)', self.argument_checker.verify_directory)

        # Credentials
        self.__database_user = self.prompt_handler.create_text_prompt(
            'Usuário do MySQL usado no Devilbox')

        database_have_password = click.confirm(
            'O usuário MySQL tem senha?', default=True)

        if database_have_password:
            self.__database_password = self.prompt_handler.create_text_prompt(
                'Senha para o usuário do MySQL')

    def __create_section(self, section_name: str):
        self.config_parser.add_section(section=section_name)

    def __create_option(self, section_name: str, option_name: str, option_value: str):
        self.config_parser.set(section_name, option_name, option_value)

    def __create_printing_instructions(self):
        instructions = {
            'paths': {
                'devilbox_root': self.__devilbox_root,
                'projects_root': self.__projects_root,
                'database_files_root': self.__database_files_root,
            },
            'credentials': {
                'database_user': self.__database_user,
                'database_password': self.__database_password
            },
        }

        return instructions

    def __create_fields_on_file(self, instructions):
        for section in instructions:
            self.__create_section(str(section))
            for option in instructions[section]:
                self.__create_option(str(section), str(
                    option), instructions[section][option])

    def __save_configuration(self, filepath):
        with open(filepath, 'wt') as config_file:
            self.config_parser.write(config_file)

    def read_field(self, section_name: str, option_name: str):
        self.config_parser.read(self.__config_file_path)
        config = self.config_parser.get(section_name, option_name)

        if not config:
            return ''

        return config

    def run(self):
        self.__promptOptions()

        click.clear()

        click.secho('Criando arquivo de configuração', fg="bright_blue")
        filepath = self.create_file(self.__config_file_path)
        click.secho('Arquivo de configuração criado', fg="green")

        click.secho('-' * 50)

        click.secho('Inserindo configurações no arquivo', fg="bright_blue")
        self.config_parser.read(filepath)
        instructions = self.__create_printing_instructions()
        self.__create_fields_on_file(instructions)
        self.__save_configuration(filepath)
        click.secho('Configurações inseridas no arquivo', fg="green")
