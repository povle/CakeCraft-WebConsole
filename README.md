# CakeCraft-WebConsole
Project for Spiralio's minecraft server "CakeCraft SMP Season 2"

## Goals to complete(Server):
- HTTP Python API server on Flask. (COMPLETED)
  * Create server with one html page.
  * Figure out how to get POST or GET data.
  * Make simple HTTP-request system.
  * Create secret key protection.
- API Base.
  * Create API-request class. (COMPLETED)
  * Make simple API-method using C++(boost/python.hpp) + Python.
- Backups.
  * Make auto-backup system.
  * Make check hash on backup.info method, so you'll know if backup is modified.
  * Make search by hash or timestamp.
  * Plug in API.
- RCON.
  * Make system to send commands to minecraft server.
  * Figure out how to get console history.
  * Plug in API.
- System statistics.
  * Figure out how to get info:
    - RAM usage.
    - CPU usage.
    - Disk usage.
  * Plug in API.
- Server manipulations.
  * Figure out how to run server remotely.
  * Plug in API.

## Goals to complete(Client):
- HTTP-requests to API by js.
- Simple(at first) html+js web-console.

## Completed(Server):
- HTTP Python API server on Flask.
  * Created server with one html page. (9.06)
  * Figured out how to get POST or GET data. (9.06)
  * Make simple HTTP-request system. (9.06)
  * Create secret key protection. (14.06)
- API Base.
  * Create API-request class. (9.06)
  * Make simple API-method using C++(boost/python.hpp) + Python. (15.06)
  - System statistics.
    * Figure out how to get info: (28.06)
      - RAM usage.
      - Disk usage.
      - Disk usage.
    * Plug in API. (28.06)
- RCON.
  * Figure out how to get console history. (29.06)
  * Make system to send commands to minecraft server. (02.07)
  * Plug in API. (02.07)
## Completed(Client):
...

## Setting up:
- At first, configure server:
```bash
cd server
./setup.sh
```

- Second thing second, each time you launch server:
```bash
cd server
./run.sh dev # other options: development, production, prod
```

Ctrl+C to exit.

- At last, if you want to get secret key browse in server/flask/app/config.json

## API Methods:
To call methods use: `https://IP:port/method/METHOD_NAME?secret=SECRET_KEY&arg1=val1&arg2=val2&...&argN=valN`, where METHOD_NAME and SECRET_KEY are name of the methods below and secret key from server/flask/app/config.json

### **stats.get_ram_usage**: returns RAM usage. Arguments:

| # | argument |   value  | description         |
|--:|:--------:|:--------:|:-------------------:|
|  1|  format  |  percent | in percents         |
|   |          | fraction | as decimal fraction |

### **stats.get_cpu_usage**: returns CPU usage. Arguments:

| # | argument |   value  | description         |
|--:|:--------:|:--------:|:-------------------:|
|  1|  format  |  percent | in percents         |
|   |          | fraction | as decimal fraction |

### **stats.get_disk_usage**: return Disk usage. Arguments:

| # | argument |   value  | description         |
|--:|:--------:|:--------:|:-------------------:|
|  1|  format  |  percent | in percents         |
|   |          | fraction | as decimal fraction |



### **rcon.exec_command**: executes command on the server. Returns console response. Arguments:

| # | argument | description |
|--:|:--------:|-------------|
|  1| command | Command to execute |

### **rcon.get_history**: returns console history. Arguments:

| # | argument | description |
|--:|:--------:|-------------|
|  1| offset | Offset from first character, 0 by default |

### **backup.make**: makes a backup of the important files. Arguments:

| # | argument | description |
|--:|:--------:|-------------|
|  1| name | Short name of backup, backup_%S_%M_%H_%d_%m by default |
|  2| desc | Full desctiption of backup, empty by default |

### **backup.info**: returns info about backup by timestamp, or the beginning of name or full name . Arguments:
| # | argument | description |
|--:|:--------:|-------------|
|  1| backup | Timestamp of backup, cannot be used with *backup_name* |
|  2| backup_name | The beginning of name or full name of backup, cannot be used with *backup* |

### **backup.list**: returns a list of backups. Arguments:

| # | argument | description |
|--:|:--------:|-------------|
|  1| count | Amount of backups to return(from the newest one), if 0 - whole list of backups |
|  2| from | Timestamp down to which backups will be displayed, 0 by default, cannot be used with *from_name* |
|  3| to | Timestamp up to which backups will be displayed, current time by default, cannot be used with *to_name* |
|  4| from_name | The beginning of name or full name down to which backups will be displayed, optional, cannot be used with *from* |
|  5| to_name | The beginning of name or full name up to which backups will be displayed, optional, cannot be used with *to* |

### **backup.switch_to**: saves current files to new backup, and then restore everything to past backup. Arguments:

| # | argument | description |
|--:|:--------:|-------------|
|  1| backup | Timestamp of backup, cannot be used with *backup_name* |
|  2| backup_name | The beginning of name or full name of backup, cannot be used with *backup* |

**WARNING: stop the server before it.**
