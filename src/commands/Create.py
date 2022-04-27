import click
from src.components.ArgumentChecker import ArgumentChecker
from src.components.DependenciesHandler import DependenciesHandler

from src.components.GitHandler import GitHandler

argument_checker = ArgumentChecker()


@click.command()
@click.option('--repo_name', prompt="Nome do projeto", required=True)
@click.option('--repo_url', prompt="URL do repositório no Git(HTTPS/SSH)", callback=argument_checker.verify_git_url, required=True)
@click.option('--master-branch', prompt="Vai clonar a branch Master?", is_flag=True, default=True)
def create(repo_name, repo_url, master_branch):
    git_handler = GitHandler(repo_name, repo_url, master_branch)
    project_directory = git_handler.run()

    dependencies_handler = DependenciesHandler(project_directory)
    dependencies_handler.run()
