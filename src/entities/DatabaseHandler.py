import os

import click


class DatabaseHandler:
    def __init__(self, db_filename, file_handler, configuration_handler) -> None:
        self.__db_filename = db_filename
        self.__formated_db_filename = db_filename + '.sql'

        self.__file_handler = file_handler
        self.__configuration_handler = configuration_handler

        self.__devilbox_root = self.__configuration_handler.read_field(
            'paths', 'devilbox_root')
        self.__devilbox_db_root = self.__get_devilbox_db_root()
        self.__configurated_db_root = self.__configuration_handler.read_field(
            'paths', 'database_files_root')

        self.__db_user = self.__configuration_handler.read_field(
            'credentials', 'database_user')
        self.__db_pass = self.__configuration_handler.read_field(
            'credentials', 'database_password')

        self.__db_file_path = os.path.join(
            self.__devilbox_db_root, self.__formated_db_filename)

    def __get_devilbox_db_root(self):
        return os.path.join(self.__devilbox_root, 'backups', 'mysql')

    def __verify_actual_path(self):
        if self.__configurated_db_root == self.__devilbox_db_root:
            return

        self.__move_file()

    def __move_file(self):
        db_file = os.path.join(self.__configurated_db_root, self.__db_filename)
        self.__file_handler.move_file(db_file, self.__devilbox_db_root)

    def __create_database(self):
        os.chdir(self.__devilbox_root)
        os.system(
            f'docker-compose exec mysql mysql -e "CREATE DATABASE {self.__db_filename};"')

    def __restore_database(self):
        os.system(
            f'docker-compose exec -T mysql mysql -h mysql -u {self.__db_user} --password={self.__db_pass} {self.__db_filename} < {self.__db_file_path}')

    def __verify_database(self):
        os.rename(self.__db_file_path, self.__db_file_path + '.old')

        self.__file_handler.replace_statments(
            self.__db_file_path + '.old', self.__db_file_path, statments={
                'utf8mb4_0900_ai_ci': 'utf8mb4_unicode_ci'
            })

    def run(self):
        self.__verify_actual_path()

        click.secho('Criando base de dados', fg="bright_blue")
        self.__create_database()
        click.secho('Base de dados criada', fg="green")

        click.secho('Verificando a base de dados', fg="bright_blue")
        self.__verify_database()
        click.secho('Base de dados verificada', fg="green")

        click.secho('Restaurando a base de dados', fg="bright_blue")
        self.__restore_database()
        click.secho('Base de dados restauradara', fg="green")
