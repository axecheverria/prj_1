from flask import Flask
from flask import request
from flask import render_template
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("my_form.html")

@app.route('/', methods=['POST'])
def my_form_post():
    youtube_url = request.form['text']

    os.system("cd #{RAILS_ROOT}/tmp/")

    # hard-coding a beyonce file for debugging
    # https://www.youtube.com/watch?v=pZ12_E5R3qc

    os.system("youtube-dl " + youtube_url) 
    os.system("ls > files.txt") 

    f = open('files.txt', 'r')
    
    while True:
        filename = f.readline()
        
        if (".mp4" in filename):
            break

        if (filename == ""):
            break

    f.close()

    return filename

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port) # app.run()
