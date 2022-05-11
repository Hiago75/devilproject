from logging import config
import os
from re import S


class HostsHandler:
    def __init__(self, project_name, configuration_handler):
        self.__project_name = project_name
        self.__configuration_handler = configuration_handler

        self.__hosts_path = self.__configuration_handler.read_field(
            'paths', 'hosts_root')

    def __verify_host(self):
        with open(self.__hosts_path, 'rt') as host:
            buf = host.readlines()

        with open(self.__hosts_path, 'wt') as new_host:
            already_inserted = False

            for line in buf:
                if '127.0.0.1' in line and not already_inserted:
                    line = line + \
                        f'127.0.0.1       {self.__project_name}.loc\n'
                    already_inserted = True
                new_host.write(line)

    def run(self):
        self.__verify_host()
