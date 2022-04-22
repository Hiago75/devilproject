import click

from src.commands.HelloWorld import hello
from src.commands.Create import create

@click.group(invoke_without_command=True)
def devilproject():
    pass

devilproject.add_command(hello)
devilproject.add_command(create)

if __name__ == '__main__':
    devilproject()