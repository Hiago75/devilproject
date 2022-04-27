import click

from src.commands.Create import create
from src.commands.Config import config


@click.group(invoke_without_command=True)
def devilproject():
    click.clear()


devilproject.add_command(create)
devilproject.add_command(config)

if __name__ == '__main__':
    devilproject()
