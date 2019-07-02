#!python3.7
import os, json, hashlib, random, time

random.seed()

class ConfigFile:
    def __init__(self):
        try:
            config_file = open("config.json", "r")
            self.config = json.load(config_file)
            config_file.close()
        except:
            config_file = open("config.json", "w")

            # config by default
            secret = hashlib.sha1()
            secret.update(str(random.randint(1000000, 999999999)).encode())
            self.config = {
                "secret_key": secret.hexdigest().upper(),
                "rcon_key": ""
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
    LOG_FILE = time.strftime("logs/%d.%m.%y.log", time.gmtime())
