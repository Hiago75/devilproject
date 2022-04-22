import click

from src.commands.HelloWorld import hello

@click.group(invoke_without_command=True)
def devilproject():
    pass

devilproject.add_command(hello)

if __name__ == '__main__':
    devilproject()