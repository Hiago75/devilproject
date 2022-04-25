import click
import os
from src.components.ArgumentChecker import ArgumentChecker
from src.components.DependenciesHandler import DependenciesHandler

from src.components.GitHandler import GitHandler

current_repository = os.getcwd()
argument_checker = ArgumentChecker()

@click.command()
@click.option('--repo_name', prompt="Nome do projeto", required=True)
@click.option('--repo_url', prompt="URL do repositório no Git(HTTPS/SSH)", callback=argument_checker.verify_git_url, required=True)
@click.option('--repo_dir', prompt="Diretório da pasta aonde será inserido o projeto", callback=argument_checker.verify_directory, default=current_repository)
def create(repo_name,repo_url,repo_dir):   
  git_handler = GitHandler(repo_name,repo_url, repo_dir)
  click.secho('Cloning repo', fg="bright_blue")
  project_directory = git_handler.clone_repo()
  click.secho('Repo cloned', fg="green")

  dependencies_handler = DependenciesHandler(project_directory)
  click.secho('Installing the dependencies', fg="bright_blue")
  dependencies_handler.run()
  click.secho('Dependencies installed', fg='green')