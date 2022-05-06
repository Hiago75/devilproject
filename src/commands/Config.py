import click

from configparser import ConfigParser

from src.components.ArgumentChecker import ArgumentChecker
from src.components.PromptHandler import PromptHandler

from src.entities.ConfigurationHandler import ConfigurationHandler

argument_checker = ArgumentChecker()
prompt_handler = PromptHandler()
config_parser = ConfigParser()
configuration_handler = ConfigurationHandler(
    prompt_handler, argument_checker, config_parser)


@click.command()
def config():
    click.clear()
    configuration_handler.run()
