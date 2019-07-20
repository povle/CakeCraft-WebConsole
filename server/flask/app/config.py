#!python3.7
import os, json, secrets, time

class ConfigFile:
    def __init__(self):
        try:
            config_file = open("config.json", "r")
            self.config = json.load(config_file)
            config_file.close()
        except:
            config_file = open("config.json", "w")

            # config by default
            secret = secrets.token_hex(20)
            self.config = {
                "secret_key": secret.upper(),
                "rcon_key": "",
                "backup_interval": 15 * 60
            }
            json.dump(self.config, config_file)

            config_file.close()

    def get(self, key):
        if key not in self.config:
            return ""
        return str(self.config[key])

config_file = ConfigFile()
print(config_file.config)

class Config(object):
    SECRET_KEY = config_file.get("secret_key")
    RCON_KEY = config_file.get("rcon_key")
    RCON_HOST = "127.0.0.1"
    RCON_PORT = 25575
    BACKUP_INTERVAL = config_file.get("backup_interval")
    LOG_FILE = time.strftime("logs/%d.%m.%y.log", time.gmtime())
