#!python3.7
from app import app, log
from flask import request
from functools import wraps
import os, json, time, secrets
import API as api_cpp

def check_secret(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        route = str(request.url_rule)
        if "secret" not in request.args:
            log.write(route + ": access denied, expected secret")
            return json.dumps({
                "bad_response": {
                    "error": "access denied, expected secret"
                }
            })
        if not secrets.compare_digest(request.args["secret"], app.config["SECRET_KEY"]): #fixed time comparison
            log.write(route+": access denied, wrong secret value: \"" + request.args["secret"] + "\"")
            return json.dumps({
                "bad_response": {
                    "error": "access denied, wrong secret value: \"" + request.args["secret"] + "\""
                }
            })
        return func(*args, **kwargs)
    return wrapper


class API:
    @app.route('/method/test', methods=['GET', 'POST'])
    @check_secret
    def test_method():
        log.write("/method/test: is working fine")
        return json.dumps({
            "response":{
                "message": "working fine"
            }
        })

    class Method:
        class Stats:
            @app.route("/method/stats.get_ram_usage", methods=['GET', 'POST'])
            @check_secret
            def get_ram_usage():
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

                result = api_cpp.stats.get_ram_usage()
                log.write("/method/stats.get_ram_usage: successful request, ram usage equal to " + str(result) + "%")
                if format == "fraction":
                    result /= 100 # 62.3% == 0.623
                return json.dumps({
                    "response":{
                        "ram_usage": result,
                        "format": format
                    }
                })

            @app.route("/method/stats.get_cpu_usage", methods=['GET', 'POST'])
            @check_secret
            def get_cpu_usage():

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

                result = api_cpp.stats.get_cpu_usage()
                log.write("/method/stats.get_cpu_usage: successful request, cpu usage equal to " + str(result) + "%")
                if format == "fraction":
                    result /= 100
                return json.dumps({
                    "response":{
                        "cpu_usage": result,
                        "format": format
                    }
                })

            @app.route("/method/stats.get_disk_usage", methods=['GET', 'POST'])
            @check_secret
            def get_disk_usage():
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

                result = api_cpp.stats.get_disk_usage()
                log.write("/method/stats.get_disk_usage: successful request, disk usage equal to " + str(result) + "%")
                if format == "fraction":
                    result /= 100
                return json.dumps({
                    "response":{
                        "disk_usage": result,
                        "format": format
                    }
                })

        class RCON:
            @app.route("/method/rcon.exec_command", methods=['GET', 'POST'])
            @check_secret
            def exec_command():
                if "command" not in request.args or request.args["command"] == "":
                    log.write("/method/rcon.exec_command: expected command")
                    return json.dumps({
                        "bad_response":{
                            "error": "expected command"
                        }
                    })
                command = request.args["command"]
                try:
                    console_response = api_cpp.rcon.exec_command(command)
                except Exception as e:
                    log.write("/method/rcon.exec_command: request failed, caught error: " + str(e))
                    return json.dumps({
                        "bad_response":{
                            "command": command,
                            "error": str(e)
                        }
                    })
                else:
                    log.write("/method/rcon.exec_command: successful request, successful command execution")
                    return json.dumps({
                        "response":{
                            "command": command,
                            "console_response": console_response
                        }
                    })

            @app.route("/method/rcon.get_history", methods=['GET', 'POST'])
            @check_secret
            def get_history():
                offset = "0" if "offset" not in request.args else request.args["offset"]
                log.write("/method/rcon.get_history: successful request")
                history = api_cpp.rcon.get_history(offset)
                return json.dumps({
                    "response":{
                        "history": history[0],
                        "chars": history[1]
                    }
                })

        # FIXME
        class BackupManagement:
            @app.route("/method/backup.make", methods=['GET', 'POST'])
            @check_secret
            def make():
                if "name" not in request.args:
                    name = None
                else:
                    name = request.args["name"]
                if "desc" not in request.args:
                    description = None
                else:
                    description = request.args["desc"]
                try:
                    backup = api_cpp.backup.make(name, description)
                except Exception as e:
                    log.write("/method/rcon.exec_command: request failed, caught error: " + str(e))
                    return json.dumps({
                        "bad_response":{
                            "error": str(e)
                        }
                    })
                else:
                    log.write("/method/rcon.exec_command: successful request, successful command execution")
                    return json.dumps({
                        "response":{
                            "backup": backup
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
