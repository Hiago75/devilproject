import os
import click


class ThemeHandler():
    def __init__(self, project_directory, prompt_handler, dependencies_handler):
        self.__prompt_handler = prompt_handler
        self.__dependencies_handler = dependencies_handler

        self.__project_directory = project_directory,
        self.__themes_directory = os.path.join(
            project_directory, 'wp-content', 'themes')

        self.__is_child = False
        self.__parent_theme = ''
        self.__main_theme = ''

        self.__parent_theme_dir = ''
        self.__main_theme_dir = ''

    def __get_theme_info(self):
        self.__is_child = click.confirm('O tema principal é um tema child?')

        if(self.__is_child):
            self.__parent_theme = self.__prompt_handler.create_text_prompt(
                'Qual o nome do tema pai?')

        self.__main_theme = self.__prompt_handler.create_text_prompt(
            'Qual o nome do tema que está sendo usado na aplicação?')

    def __get_themes_path(self):
        if self.__is_child:
            self.__parent_theme_dir = os.path.join(
                self.__themes_directory, self.__parent_theme)

        self.__main_theme_dir = os.path.join(
            self.__themes_directory, self.__main_theme)

    def __yarn_build(self, theme_dir):
        os.chdir(theme_dir)
        os.system('yarn build')

    def __build_theme(self, theme_directory):
        self.__dependencies_handler.yarn_install(theme_directory)
        self.__dependencies_handler.composer_install(theme_directory)
        self.__yarn_build(theme_directory)

    def run(self):
        click.clear()
        self.__get_theme_info()

        click.secho('Pegando o(s) diretório(s) do(s) tema(s)', fg='bright_blue')
        self.__get_themes_path()
        click.secho('Diretório(s) pego(s)', fg="green")
        
        click.secho('Instalando dependencias e buildando o(s) tema(s)', fg="bright_blue")
        if self.__is_child:
            self.__build_theme(self.__parent_theme_dir)

        self.__build_theme(self.__main_theme_dir)
        click.secho('Dependencias instaladas e tema(s) buildado(s)')