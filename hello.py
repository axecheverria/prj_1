import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("my_form.html")
