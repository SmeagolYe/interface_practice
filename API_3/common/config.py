import configparser
from API_3.common import constants


class ReadConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(constants.global_conf_dir)
        switch = self.config.getboolean('switch', 'on')
        if switch:
            self.config.read(constants.online_conf_dir)
        else:
            self.config.read(constants.test_conf_dir)

    def get(self, section, option):
        return self.config.get(section, option)


config = ReadConfig()
