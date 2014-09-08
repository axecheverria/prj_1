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
    text = request.form['text']
    multiply_text = text * 4


    os.system("cd #{RAILS_ROOT}/tmp/")
    os.system("mkdir ./musicFiles")
    os.system("cd ./musicFiles")

    # s = os.system("ls -lt")
    os.system("youtube-dl https://www.youtube.com/watch?v=pZ12_E5R3qc") 
    # os.system("curl -o ./myfile.png 'http://colorlib.com/wp/wp-content/uploads/2014/02/Olympic-logo.png'") 

    # for i in range (0, 5):
        # os.system("touch " + str(i) + ".txt")

    # p = subprocess.Popen("ls -t | head -1", stdout=subprocess.PIPE, shell=True)
    p = subprocess.Popen("pwd", stdout=subprocess.PIPE, shell=True)
    # p = subprocess.Popen("ls", stdout=subprocess.PIPE, shell=True)

    # curious, what is runtime.txt?

    (filename, err) = p.communicate()
    return filename

    # return multiply_text
    # return "test" 

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port) # app.run()
