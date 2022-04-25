import click

from src.commands.Create import create

@click.group(invoke_without_command=True)
def devilproject():
    click.clear()

devilproject.add_command(create)

if __name__ == '__main__':
    devilproject()