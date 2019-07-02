#!python3.7
from API import api_cpp
from app import app, log

import shutil, os, tarfile, mcrcon, json, time, atexit
from apscheduler.schedulers.background import BackgroundScheduler

def greet():
    return api_cpp.greet()

class Stats(api_cpp.stats):
    pass
stats = Stats()
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
            raise e
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
rcon = RCON()
class Backup(api_cpp.backup):
    @staticmethod
    def make(name = None, desc = None):
        if name == None:
            name = time.strftime("backup_%H:%M:%S:.%d.%m.%y", time.gmtime())
        if desc == None:
            desc = ""
        # FIXME: {
        try:
            response = rcon.exec_command("save-all") # IF SERVER ISN'T WORKING THEN DOES NOT MATTER
        except Exception as e:
            log.write("Backup.make: couldn't save all, error: " + str(e))
        else:
            log.write("Backup.make: saved all, result: " + response)
        # }
        prefix = "../minecraft/"
        fname = "../minecraft-backups/" + name.replace(" ", "_")
        if os.path.isfile(fname + ".json") or os.path.isfile(fname + ".tar.gz"):
            return ("That name is already in use")
        f = open(fname + ".json", "w")
        info = {
            "name": name,
            "description": desc,
            "timestamp": int(time.time())
        }
        json.dump(info, f)
        backup = tarfile.open(fname + ".tar.gz", "w:gz")
        try:
            to_save = [
                "crash-reports/",
                "logs/",
                "plugins/",
                "world/",
                "world_nether/",
                "world_the_end/",
                "banned-ips.json",
                "banned-players.json",
                "bukkit.yml",
                "commands.yml",
                "eula.txt",
                "help.yml",
                "ops.json",
                "paper.yml",
                "permissions.yml",
                "server.properties",
                "spigot.yml",
                "usercache.json",
                "version_history.json",
                "whitelist.json",
            ]
            for i in to_save:
                backup.add(prefix + i, arcname=i)
            backup.close()
        except Exception as e:
            log.write("Backup.make: backup failed")
            raise e
        else:
            backup.close()
            log.write("Backup.make: backup made successfully")
        return info
    @staticmethod
    def info(backup, backup_name):
        pass
    @staticmethod
    def list(count, from_date, to_date, from_name, to_name):
        pass
    @staticmethod
    def switch_to(backup, backup_name, force):
        pass
backup = Backup()
if os.environ.get("FLASK_ENV") != "development":
    def AUTO_BACKUP():
        backup.make(None, "AUTO BACKUP: Save made by script to prevent any casualities")
    AUTO_BACKUP()
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=AUTO_BACKUP, trigger="interval", seconds=int(app.config["BACKUP_INTERVAL"]))
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown())
    log.write("Auto backup enabled")
else:
    log.write("Auto backup disabled")
