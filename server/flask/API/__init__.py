#!python
from API import api_cpp

def greet():
    return api_cpp.greet()

stats = api_cpp.stats()
rcon = api_cpp.rcon()
backup = api_cpp.backup()
