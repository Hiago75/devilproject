import os
import click

from configparser import ConfigParser

from src.components.FileHandler import FileHandler


class ConfigurationHandler(FileHandler):
    def __init__(self) -> None:
        FileHandler.__init__(self)
        self.config_file_path = os.path.join(
            self.assets_folder, 'config.ini')
        self.config_parser = ConfigParser()

    def create_section(self, section_name):
        self.config_parser.add_section(section=section_name)

    def create_option(self, section_name, option_name, option_value):
        self.config_parser.set(section_name, option_name, option_value)

    def save_configuration(self, filepath):
        with open(filepath, 'wt') as config_file:
            self.config_parser.write(config_file)

    def run(self, devilbox_root):
        filepath = self.create_file(self.config_file_path)
        self.config_parser.read(filepath)
        self.create_section('paths')
        self.create_option('paths', 'devilbox_root', devilbox_root)
        self.save_configuration(filepath)
