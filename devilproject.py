import click

from src.HelloWorld import HelloWorld

@click.command()
def devilproject():
    HelloWorld()
            
