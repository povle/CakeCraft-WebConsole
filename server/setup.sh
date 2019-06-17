#!/usr/bin/bash

# C++:
cd cpp
sudo apt install g++ make cmake
cmake .
make
cd ..

# Python:
cd flask
mkdir logs

# We are going to need this
sudo apt install python3.7-dev python3.7
python3.7 -V

# Setting up virtual environment

sudo apt install python3-venv
python3.7 -m venv venv
source venv/bin/activate
sudo apt install python3-pip
pip3 install Flask
python3.7 -m flask --version
deactivate
