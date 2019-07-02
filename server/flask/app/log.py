#!python3.7
from app import app
import time

def write(message):
    try:
        log_file = open(app.config["LOG_FILE"], "a")
    except:
        raise
    message = time.strftime("[%H:%M:%S] ", time.gmtime()) + message
    print("")
    print(message)
    print("")
    log_file.write(message)
    log_file.write("\n")
    log_file.close()
