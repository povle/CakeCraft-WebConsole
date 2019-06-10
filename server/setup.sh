#!/usr/bin/bash
sudo apt install python3
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
sudo apt install python3-flask
deactivate
