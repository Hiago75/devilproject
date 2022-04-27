from email.policy import default
import click

from src.entities.ConfigurationHandler import ConfigurationHandler

configuration_handler = ConfigurationHandler()


@click.command()
@click.option('--devilbox_root', prompt="Diretório raiz do devilbox (caminho completo)", help="O diretório aonde você clonou o devilbox. Deve ser inserido como o caminho completo (/home/user/devilbox)")
@click.option('--database_user', prompt="Usuário do MySQL usado no Devilbox", help="Usuário que foi criado e configurado dentro da instancia do MySQL do próprio Devilbox", default="root")
def config(devilbox_root, database_user):
    configuration_handler.run(devilbox_root, database_user)
