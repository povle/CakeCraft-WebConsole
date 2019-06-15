#!/usr/bin/bash
cd flask
mkdir logs

# We are going to need this
sudo apt install python3
python3 -V

# Setting up virtual environment

sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
sudo apt install python3-pip
pip3 install Flask
python3 -m flask --version
deactivate
