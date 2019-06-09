import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "Foom5eDahl0ya5neiqu8aip6aikoeZoo"
