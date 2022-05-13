from configparser import ConfigParser
from sqlite3 import DatabaseError
from time import sleep
import click

from src.components.ArgumentChecker import ArgumentChecker
from src.components.FileHandler import FileHandler
from src.components.PromptHandler import PromptHandler
from src.entities.DatabaseHandler import DatabaseHandler

from src.entities.GitHandler import GitHandler
from src.components.DependenciesHandler import DependenciesHandler
from src.entities.HostsHandler import HostsHandler
from src.entities.SetupChecker import SetupChecker
from src.entities.ThemeHandler import ThemeHandler
from src.entities.WordPressConfigHandler import WordPressConfigHandler
from src.entities.ConfigurationHandler import ConfigurationHandler

argument_checker = ArgumentChecker()
setup_checker = SetupChecker()
prompt_handler = PromptHandler()
config_parser = ConfigParser()
file_handler = FileHandler()
configuration_handler = ConfigurationHandler(
    prompt_handler, argument_checker, config_parser)


@click.command()
def create():
    setup_checker.run()

    git_handler = GitHandler(
        prompt_handler, argument_checker, configuration_handler)
    project_directory, project_name = git_handler.run()

    dependencies_handler = DependenciesHandler(file_handler)
    click.secho('Instalando as dependencias do composer',
                fg="bright_blue")
    dependencies_handler.composer_install(project_directory)
    click.secho('Dependencias instaladas', fg='green')
    sleep(2)
    click.clear()

    wordpress_config_handler = WordPressConfigHandler(
        project_name, project_directory, configuration_handler)
    db_filename = wordpress_config_handler.run()

    database_handler = DatabaseHandler(
        db_filename, file_handler, configuration_handler)
    database_handler.run()

    hosts_handler = HostsHandler(project_name, configuration_handler)
    hosts_handler.run()

    theme_handler = ThemeHandler(
        project_directory, prompt_handler, dependencies_handler, file_handler)
    theme_handler.run()

    click.echo('-' * 50)
    click.secho('Tudo pronto', fg="green")
