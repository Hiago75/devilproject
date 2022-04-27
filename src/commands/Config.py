from email.policy import default
import click

from src.entities.ConfigurationHandler import ConfigurationHandler

configuration_handler = ConfigurationHandler()


@click.command()
def config():
    click.clear()
    configuration_handler.run()
