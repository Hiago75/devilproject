from configparser import ConfigParser
import click

from src.components.ArgumentChecker import ArgumentChecker
from src.components.PromptHandler import PromptHandler

from src.entities.GitHandler import GitHandler
from src.entities.DependenciesHandler import DependenciesHandler
from src.entities.SetupChecker import SetupChecker
from src.entities.WordPressConfigHandler import WordPressConfigHandler
from src.entities.ConfigurationHandler import ConfigurationHandler

argument_checker = ArgumentChecker()
setup_checker = SetupChecker()
prompt_handler = PromptHandler()
config_parser = ConfigParser()
# TODO: Create a way to read the configuration file without instancing the ConfigurationHandler
configuration_handler = ConfigurationHandler(
    prompt_handler, argument_checker, config_parser)


@click.command()
def create():
    setup_checker.run()

    git_handler = GitHandler(
        prompt_handler, argument_checker, configuration_handler)
    project_directory, project_name = git_handler.run()

    dependencies_handler = DependenciesHandler(project_directory)
    dependencies_handler.run()

    wordpress_config_handler = WordPressConfigHandler(
        project_name, project_directory, configuration_handler)
    wordpress_config_handler.run()

    click.echo('-' * 50)
    click.secho('Tudo pronto', fg="green")
