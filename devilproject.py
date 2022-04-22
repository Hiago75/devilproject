import click

from src.HelloWorld import hello

@click.group(invoke_without_command=True)
def devilproject():
    pass

devilproject.add_command(hello)