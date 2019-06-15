#!python3.7
from app import app, log
from flask import request
import os, json, time
import API as api_cpp

"""
@app.route('/')
@app.route('/index')
def index():
    f = open("/app/index.html")
    page = f.read()
    f.close()
    return page

@app.route("/method/new")
def new_method():
    r = ""
    for i in range(1, 11):
        r += str(i) + "\t" + str(i*i) + "<br/>"
    return r
"""

def check_secret(secret):
    if secret == app.config["SECRET_KEY"]:
        return True # Secret is right
    return False # Somebody is trying to hack us! :(

class API:
    @app.route('/method/test', methods=['GET', 'POST'])
    def test_method():
        if "secret" not in request.args:
            log.write("/method/test: access denied, expected secret")
            return json.dumps({
                "bad_response": {
                    "error": "access denied, expected secret"
                }
            })
        if not check_secret(request.args["secret"]):
            log.write("/method/test: access denied, wrong secret value: \"" + request.args["secret"] + "\"")
            return json.dumps({
                "bad_response": {
                    "error": "access denied, wrong secret value: \"" + request.args["secret"] + "\""
                }
            })
        log.write("/method/test: is working fine")
        return json.dumps({
            "response":{
                "message": "working fine, {}".format(api_cpp.stats.get_ram_usage())
            }
        })

    class Method:
        class Stats:
            @app.route("/method/stats.get_ram_usage", methods=['GET', 'POST'])
            def get_ram_usage():

                if "secret" not in request.args:
                    log.write("/method/stats.get_ram_usage: access denied, expected secret")
                    return json.dumps({
                        "bad_response":{
                            "error": "access denied, expected secret"
                        }
                    })
                if not check_secret(request.args["secret"]):
                    log.write("/method/stats.get_ram_usage: access denied, wrong secret value: \"" + request.args["secret"] + "\"")
                    return json.dumps({
                        "bad_response":{
                            "error": "access denied, wrong secret value: \"" + request.args["secret"] + "\""
                        }
                    })
                if "format" not in request.args:
                    format = "fraction"
                elif request.args["format"] not in ["percent", "fraction"]:
                    log.write("/method/stats.get_ram_usage: wrong format value")
                    return json.dumps({
                        "bad_response":{
                            "error": "wrong format value, expected \"percent\" or \"fraction\""
                        }
                    })
                else:
                    format = request.args["format"]

                # FIXME
                result = 62.3
                log.write("/method/stats.get_ram_usage: successful request, ram usage equal to " + result + "%")
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

                if "secret" not in request.args:
                    log.write("/method/stats.get_cpu_usage: access denied, expected secret")
                    return json.dumps({
                        "bad_response":{
                            "error": "access denied, expected secret"
                        }
                    })
                if not check_secret(request.args["secret"]):
                    log.write("/method/stats.get_cpu_usage: access denied, wrong secret value: \"" + request.args["secret"] + "\"")
                    return json.dumps({
                        "bad_response":{
                            "error": "access denied, wrong secret value: \"" + request.args["secret"] + "\""
                        }
                    })
                if "format" not in request.args:
                    format = "fraction"
                elif request.args["format"] not in ["percent", "fraction"]:
                    log.write("/method/stats.get_cpu_usage: wrong format value")
                    return json.dumps({
                        "bad_response":{
                            "error": "wrong format value, expected \"percent\" or \"fraction\""
                        }
                    })
                else:
                    format = request.args["format"]

                # FIXME
                result = 56.3
                log.write("/method/stats.get_cpu_usage: successful request, cpu usage equal to " + result + "%")
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

                if "secret" not in request.args:
                    log.write("/method/stats.get_disk_usage: access denied, expected secret")
                    return json.dumps({
                        "bad_response":{
                            "error": "access denied, expected secret"
                        }
                    })
                if not check_secret(request.args["secret"]):
                    log.write("/method/stats.get_disk_usage: access denied, wrong secret value: \"" + request.args["secret"] + "\"")
                    return json.dumps({
                        "bad_response":{
                            "error": "access denied, wrong secret value: \"" + request.args["secret"] + "\""
                        }
                    })
                if "format" not in request.args:
                    format = "fraction"
                elif request.args["format"] not in ["percent", "fraction"]:
                    log.write("/method/stats.get_disk_usage: wrong format value")
                    return json.dumps({
                        "bad_response":{
                            "error": "wrong format value, expected \"percent\" or \"fraction\""
                        }
                    })
                else:
                    format = request.args["format"]

                # FIXME
                result = 72.3
                log.write("/method/stats.get_disk_usage: successful request, disk usage equal to " + result + "%")
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

                if "secret" not in request.args:
                    log.write("/method/rcon.exec_command: access denied, expected secret")
                    return json.dumps({
                        "bad_response":{
                            "error": "access denied, expected secret"
                        }
                    })
                if not check_secret(request.args["secret"]):
                    log.write("/method/rcon.exec_command: access denied, wrong secret value: \"" + request.args["secret"] + "\"")
                    return json.dumps({
                        "bad_response":{
                            "error": "access denied, wrong secret value: \"" + request.args["secret"] + "\""
                        }
                    })
                if "command" not in request.args or request.args["command"] == "":
                    log.write("/method/rcon.exec_command: expected command")
                    return json.dumps({
                        "bad_response":{
                            "error": "expected command"
                        }
                    })
                command = request.args["command"]
                # FIXME
                # Temporary part to allow web-developer do his job:
                console_response = "Unrecognized command \"" + command.split()[0] + "\".\n"
                try:
                    console_history = open("temp_console_history.json", "r")
                    history = json.load(console_history)
                    console_history.close()
                except IOError:
                    history = {"msg":[]}
                except:
                    raise
                history["msg"].append({
                    "type":"command",
                    "timestamp": time.time(),
                    "command":command,
                    "console_response":console_response
                })
                try:
                    console_history = open("temp_console_history.json", "w")
                    json.dump(history, console_history, indent=4)
                    console_history.close()
                except:
                    raise
                # End of temporary part
                log.write("/method/rcon.exec_command: successful request, successful command execution")
                return json.dumps({
                    "response":{
                        "command": command,
                        "console_response": console_response
                    }
                })

            # FIXME
            @app.route("/method/rcon.get_history", methods=['GET', 'POST'])
            def get_history():

                if "secret" not in request.args:
                    log.write("/method/rcon.get_history: access denied, expected secret")
                    return json.dumps({
                        "bad_response":{
                            "error": "access denied, expected secret"
                        }
                    })
                if not check_secret(request.args["secret"]):
                    log.write("/method/rcon.get_history: access denied, wrong secret value: \"" + request.args["secret"] + "\"")
                    return json.dumps({
                        "bad_response":{
                            "error": "access denied, wrong secret value: \"" + request.args["secret"] + "\""
                        }
                    })
                # FIXME
                # Temporary part to allow web-developer do his job:
                try:
                    console_history = open("temp_console_history.json", "r")
                    history = json.load(console_history)["msg"]
                    console_history.close()
                except IOError:
                    history = {"msg":[]}
                except:
                    raise
                # End of temporary part
                history.sort(key=lambda x: x["timestamp"])
                log.write("/method/rcon.get_history: successful request")
                return json.dumps({
                    "response":{
                        "history": history
                    }
                })

        # FIXME
        class BackupManagement:
            @app.route("/method/backup.make", methods=['GET', 'POST'])
            def make():
                log.write("/method/backup.make: API method does not work, W.I.P.")
                return json.dumps({
                    "bad_response":{
                        "error": "API method W.I.P."
                    }
                })

            @app.route("/method/backup.info", methods=['GET', 'POST'])
            def info():
                log.write("/method/backup.make: API method does not work, W.I.P.")
                return json.dumps({
                    "bad_response":{
                        "error": "API method W.I.P."
                    }
                })

            @app.route("/method/backup.list", methods=['GET', 'POST'])
            def list():
                log.write("/method/backup.make: API method does not work, W.I.P.")
                return json.dumps({
                    "bad_response":{
                        "error": "API method W.I.P."
                    }
                })

            @app.route("/method/backup.switch_to", methods=['GET', 'POST'])
            def switch_to():
                log.write("/method/backup.make: API method does not work, W.I.P.")
                return json.dumps({
                    "bad_response":{
                        "error": "API method W.I.P."
                    }
                })
