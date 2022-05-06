import re
import os
import click

from git import Repo

from src.components.ArgumentChecker import ArgumentChecker
from src.components.PromptHandler import PromptHandler


class GitHandler:
    def __init__(self, prompt_handler, argument_checker, configuration_handler) -> None:
        self.__repo_url = None
        self.__repo_name = None
        self.__master_branch = None
        self.__repo_directory = None

        self.__prompt_handler = prompt_handler
        self.__argument_checker = argument_checker
        self.__configuration_handler = configuration_handler

        self.__devilbox_data_path = self.__configuration_handler.read_field(
            'paths', 'projects_root')

    def __prompt_options(self):
        self.__repo_name = self.__prompt_handler.create_text_prompt(
            'Qual o nome do projeto?')
        self.__repo_url = self.__prompt_handler.create_text_prompt(
            'Qual a URL do repositório Git(HTTPS/SSH)?', self.__argument_checker.verify_git_url)
        self.__master_branch = click.confirm(
            'Vai clonar a branch Master?', default=True)
        self.__repo_directory = click.prompt(
            'Diretório da pasta aonde será inserido o projeto', default=self.__devilbox_data_path)

    def __filter_repo_name(self) -> str:
        filtered_name = re.sub('[^A-Za-z0-9]+', '', self.__repo_name)
        return filtered_name.lower()

    def __handle_branch(self) -> str:
        branch = 'master'

        if not self.__master_branch:
            branch = click.prompt(
                'Qual o nome da branch que você quer clonar?')

        return branch

    def __handle_repo_directory(self) -> str:
        self.__argument_checker.verify_directory(self.__repo_directory)
        filtered_repo_name = self.__filter_repo_name()

        complete_directory = os.path.join(
            self.__repo_directory, filtered_repo_name)
        already_exists = self.__argument_checker.verify_git_directory(
            complete_directory)

        if already_exists:
            exit()

        return complete_directory

    def __clone_repo(self, directory, branch):
        Repo.clone_from(self.__repo_url, directory, branch=branch)

    def run(self):
        self.__prompt_options()
        branch = self.__handle_branch()
        directory = self.__handle_repo_directory()
        click.clear()

        click.secho('Clonando o repositório', fg="bright_blue")
        self.__clone_repo(directory, branch)
        click.secho('Repositório clonado', fg="green")

        return directory, self.__repo_name
