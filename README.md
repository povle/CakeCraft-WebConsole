# CakeCraft-WebConsole
Project for Spiralio's minecraft server "CakeCraft SMP Season 2"
## Goals to complete(Server):
- HTTP Python API server on Flask.
  1. Create server with one html page.
  2. Figure out how to get POST or GET data.
  3. Make simple HTTP-request system.
  4. Create no-https protection (using md5, secret key, etc.).
- API Base.
  1. Create API-request class.
  2. Make simple API-method using C++(boost/python.hpp) + Python.
- Backups.
  1. Make auto-backup system.
  2. Plug in API.
- RCON.
  1. Make system to send commands to minecraft server.
  2. Figure out how to get console history.
  3. Plug in API.
- System statistics.
  1. Figure out how to get info:
    - RAM usage.
    - CPU usage.
    - Disk usage.
  2. Plug in API.
## Goals to complete(Client):
- HTTP-requests to API by js.
- Simple(at first) html+js web-console.
## Completed(Server):
- HTTP Python API server on Flask.
  1. Created server with one html page.
  2. Figured out how to get POST or GET data.
## Completed(Client):
...
## Comments:
- To configure server use server/setup.sh (run in Server directory!).
- To launch server use server/run.sh (run in Server directory!), Ctrl+C to exit.
- Also you must run
```bash
source venv/bin/activate
export FLASK_APP=main.py
FLASK_ENV=production # or development
deactivate
```
## API Methods:
To call methods use:
http://IP:port/methhod/*METHOD_NAME*?secret=*SECRET*&arg1=val1&arg2=val2&...&argN=valN, where *SECRET* is md5(secret_key+":"+arg1+"="+val1+","+arg2+"="+val2+","+...+argN+valN+".")
1. *get_ram_usage*: returns RAM usage. Arguments:

| argument |   value  | description |
|:--------:|:--------:|:-----------:|
|  format  |  percent | in percents |
|          | fraction | as decimal fraction |
