# app/core/config.py
import os
import configparser
from pathlib import Path


class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        config_path = os.path.join(Path(__file__).parent.parent, "config.ini")

        if not os.path.exists(config_path):
            raise FileNotFoundError("Создайте файл config.ini в корне проекта!")

        self.config.read(config_path)

    def get_bybit_keys(self):
        return {
            "api_key": self.config["bybit"]["api_key"],
            "api_secret": self.config["bybit"]["api_secret"],
        }

    def get_database_path(self):
        return self.config["database"]["path"]

    def get_cache_ttl(self):
        return int(self.config["app"]["cache_ttl"])


settings = Config()
