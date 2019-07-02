#!python3.7
from API import api_cpp
from app import app
import mcrcon


def greet():
    return api_cpp.greet()

class Stats(api_cpp.stats):
    pass
class RCON(api_cpp.rcon):
    @staticmethod
    def exec_command(command):
        response = ""
        mcr = mcrcon.MCRcon(app.config["RCON_HOST"], app.config["RCON_KEY"])
        try:
            mcr.connect()
            response = mcr.command(command)
            mcr.disconnect()
        except Exception as e:
            response += "\n" + str(e)
        finally:
            mcr.disconnect()
        return response
    @staticmethod
    def get_history(offset):
        try:
            f = open("../minecraft/logs/latest.log")
            f.seek(int(offset), 0)
            t = f.read()
            f.close()
            return (t, len(t))
        except:
            return ("ERROR when open latest.log", 0)
class Backup(api_cpp.backup):
    pass

stats = Stats()
backup = Backup()
rcon = RCON()
