import os
import re
import click

class ArgumentChecker:
  def verify_git_url(self, ctx, param, url):
    git_ssh_url = bool(re.match(r"^(git@github.com:).+(.git)$", url, flags=re.M))
    git_https_rul = bool(re.match(r"^(https://github.com).+(.git)$", url, flags=re.M))

    if git_ssh_url or git_https_rul:
      return url
    
    raise click.BadParameter('A URL fornecida possui um formato inválido')
    
  def verify_directory(self,ctx,param,dir):
    directory_exists = os.path.exists(dir)

    if directory_exists:
      print('Diretório existe')

    raise click.BadParameter('Esse diretório não existe. Confira se o caminho está completo e escrito corretamente') 