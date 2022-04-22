import click
import os

from src.components.GitHandler import GitHandler

current_repository = os.getcwd()

@click.command()
@click.option('--repo_name', prompt="Project name", required=True)
@click.option('--repo_url', prompt="Github repo URL", required=True)
@click.option('--repo_dir', prompt="Project directory", required=True, default=current_repository)
def create(repo_name,repo_url,repo_dir): 
  git_handler = GitHandler(repo_name,repo_url, repo_dir)
  git_handler.clone_repo()