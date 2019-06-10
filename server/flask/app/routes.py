#!python3
from app import app
from flask import request
import os, json, time

"""
@app.route('/')
@app.route('/index')
def index():
    f = open(os.getcwd() + "/app/index.html")
    page = f.read()
    f.close()
    return page


@app.route('/method/test', methods=['GET', 'POST'])
def test_method():
    return "Hello, world!<br/>Also hi, " + request.args["user.name"] + "!"

@app.route("/method/new")
def new_method():
    r = ""
    for i in range(1, 11):
        r += str(i) + "\t" + str(i*i) + "<br/>"
    return r
"""
class API:
    class Method:
        class Statistics:
            @app.route("/method/stats.get_ram_usage", methods=['GET', 'POST'])
            def get_ram_usage():

                if "format" not in request.args:
                    format = "fraction"
                elif request.args["format"] not in ["percent", "fraction"]:
                    return json.dumps({
                        "bad_response":{
                            "error": "wrong format argument in GET/POST args, expected \"percent\" or \"fraction\""
                        }
                    })
                else:
                    format = request.args["format"]

                result = 62.3
                if format == "fraction":
                    result /= 100 # 62.3% == 0.623
                return json.dumps({
                    "response":{
                        "ram_usage": result,
                        "format": format
                    }
                })

            @app.route("/method/stats.get_cpu_usage", methods=['GET', 'POST'])
            def get_cpu_usage():

                if "format" not in request.args:
                    format = "fraction"
                elif request.args["format"] not in ["percent", "fraction"]:
                    return json.dumps({
                        "bad_response":{
                            "error": "wrong format argument in GET/POST args, expected \"percent\" or \"fraction\""
                        }
                    })
                else:
                    format = request.args["format"]

                result = 56.3
                if format == "fraction":
                    result /= 100
                return json.dumps({
                    "response":{
                        "ram_usage": result,
                        "format": format
                    }
                })

            @app.route("/method/stats.get_disk_usage", methods=['GET', 'POST'])
            def get_disk_usage():

                if "format" not in request.args:
                    format = "fraction"
                elif request.args["format"] not in ["percent", "fraction"]:
                    return json.dumps({
                        "bad_response":{
                            "error": "wrong format argument in GET/POST args, expected \"percent\" or \"fraction\""
                        }
                    })
                else:
                    format = request.args["format"]

                result = 82.1
                if format == "fraction":
                    result /= 100
                return json.dumps({
                    "response":{
                        "ram_usage": result,
                        "format": format
                    }
                })

        # FIXME
        class RCON:
            @app.route("/method/rcon.exec_command", methods=['GET', 'POST'])
            def exec_command():

                if "command" not in request.args or request.args["command"] == "":
                    return json.dumps({
                        "bad_response":{
                            "error": "expected command argument in GET/POST args"
                        }
                    })
                command = request.args["command"]
                # FIXME
                # Temporary part to allow web-developer do his job:
                console_response = "Unrecognized command \"" + command.split()[0] + "\".\n"
                with open(os.getcwd() + "/temp_console-history.json", "r") as f:
                    history = json.loads(f.read())
                history["msg"].append({
                    "type":"command",
                    "timestamp": time.time(),
                    "command":command,
                    "console_response":console_response
                })
                with open(os.getcwd() + "/temp_console-history.json", "w") as f:
                    json.dump(history, f, indent=4)
                # End of temporary part
                return json.dumps({
                    "response":{
                        "command": command,
                        "console_response": console_response
                    }
                })

            @app.route("/method/rcon.get_history", methods=['GET', 'POST'])
            def get_history():

                # FIXME
                # Temporary part to allow web-developer do his job:
                with open(os.getcwd() + "/temp_console-history.json", "r") as f:
                    history = json.loads(f.read())["msg"]
                # End of temporary part
                history.sort(key=lambda x: x["timestamp"])
                return json.dumps({
                    "response":{
                        "history":history
                    }
                })

        # FIXME
        class BackupManagement:
            @app.route("/method/backup.make", methods=['GET', 'POST'])
            def make():

                # FIXME
                if True:
                    name = "backup_" + time.strftime("%H:%M:%S_%d.%m.%y", time.gmtime())
                # FIXME
                # Temporary part to allow web-developer do his job:

                # End of temporary part
                # FIXME
                size = 0
                #size = os.path.getsize(os.getcwd() + "/../backups/" + name + "/") # Size of archive
                return json.dumps({
                    "response":{
                        "name": name,
                        "hash": 0xFFFFFFFF,
                        "path": "/server/backups/" + name + "/",
                        "size": size
                    }
                })


            @app.route("/method/backup.info", methods=['GET', 'POST'])
            def info():

                return json.dumps(None)

            @app.route("/method/backup.list", methods=['GET', 'POST'])
            def list():

                return json.dumps(None)


            @app.route("/method/backup.switch_to", methods=['GET', 'POST'])
            def switch_to():

                return json.dumps(None)
