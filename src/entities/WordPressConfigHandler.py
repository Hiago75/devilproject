import click
from src.components.FileHandler import FileHandler


class WordPressConfigHandler:
    def __init__(self, project_directory) -> None:
        self.project_directory = project_directory
        self.file_handler = FileHandler()

    def create_base_file(self):
        self.file_handler.copy_asset_file(
            'wp-config.php', self.project_directory)

    def run(self):
        click.secho(
            'Criando o arquivo de configuração do wordpress', fg="bright_blue")
        self.create_base_file()
        click.secho('Arquivo de configuração criado', fg="green")
