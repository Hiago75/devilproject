import click

from src.entities.ConfigurationHandler import ConfigurationHandler

configuration_handler = ConfigurationHandler()


@click.command()
@click.option('--devilbox_root', prompt="Diretório raiz do devilbox (caminho completo)", help="O diretório aonde você clonou o devilbox. Deve ser inserido como o caminho completo (/home/user/devilbox)")
def config(devilbox_root):
    configuration_handler.run(devilbox_root)
