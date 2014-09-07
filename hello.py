from flask import Flask
from flask import request
from flask import render_template
import os
import subprocess


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("my_form.html")
