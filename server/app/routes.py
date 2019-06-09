#!python3
from app import app
from flask import request
import os
import json

@app.route('/')
@app.route('/index')
def index():
    f = open(os.getcwd() + "/app/index.html")
    page = f.read()
    f.close()
    return page


@app.route('/method/test', methods=['GET', 'POST'])
def test_method():
    return "Hello, world!<br/>Also hi, " + request.args["user.name"] + "!"

@app.route("/method/new")
def new_method():
    r = ""
    for i in range(1, 11):
        r += str(i) + "\t" + str(i*i) + "<br/>"
    return r
