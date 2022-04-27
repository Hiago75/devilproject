import re
import os
import click
from git import Repo

from src.components.ArgumentChecker import ArgumentChecker


class GitHandler:
    def __init__(self, repo_name: str, repo_url: str, master_branch: bool) -> None:
        self.repo_url = repo_url
        self.repo_name = repo_name
        self.master_branch = master_branch

        self.argument_checker = ArgumentChecker()

    def filter_repo_name(self) -> str:
        filtered_name = re.sub('[^A-Za-z0-9]+', '', self.repo_name)
        return filtered_name.lower()

    def handle_branch(self) -> str:
        branch = 'master'

        if not self.master_branch:
            branch = click.prompt(
                'Qual o nome da branch que você quer clonar?')

        return branch

    def handle_repo_directory(self) -> str:
        current_repository = os.getcwd()
        repo_directory = click.prompt(
            'Diretório da pasta aonde será inserido o projeto', default=current_repository)

        self.argument_checker.verify_directory(repo_directory)
        filtered_repo_name = self.filter_repo_name()

        complete_directory = os.path.join(
            repo_directory, filtered_repo_name)

        return complete_directory

    def clone_repo(self, directory, branch):
        Repo.clone_from(self.repo_url, directory, branch=branch)

    def run(self):
        branch = self.handle_branch()
        directory = self.handle_repo_directory()
        click.clear()

        click.secho('Clonando o repositório', fg="bright_blue")
        self.clone_repo(directory, branch)
        click.secho('Repositório clonado', fg="green")

        return directory
