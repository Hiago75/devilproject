from email.policy import default
import click

@click.command()
@click.option('--name', default='USER', prompt="Your name")
def hello(name):
    print("Hellow World and hello " + name)