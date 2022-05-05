import os
import re
import click


class ArgumentChecker:
    def verify_git_url(self, url):
        git_ssh_url = bool(
            re.match(r"^(git@github.com:).+(.git)$", url, flags=re.M))
        git_https_url = bool(
            re.match(r"^(https://github.com).+(.git)$", url, flags=re.M))

        if git_ssh_url or git_https_url:
            return True

        click.secho(
            'Essa URL não é válida. Verifique o formato e se ela está escrita corretamente', fg="red")
        return False

    def verify_directory(self, dir):
        directory_exists = os.path.exists(dir)

        if directory_exists:
            return True

        click.secho(
            'Esse diretório não existe. Confira se o caminho está completo e escrito corretamente', fg="red")
        return False
