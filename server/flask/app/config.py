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
            }
            json.dump(self.config, config_file)

            config_file.close()
            
    def get(self, key):
        if key not in self.config:
            return ""
        try:
            return str(self.config[key])
        except:
            raise

config_file = ConfigFile()
print(config_file.config)

class Config(object):
    SECRET_KEY = config_file.get("secret_key")
    LOG_FILE = time.strftime("logs/%d.%m.%y.log", time.gmtime())
