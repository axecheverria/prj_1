import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("my_form.html")

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    multiply_text = text * 3
    
    return multiply_text
    # youtube_url = request.form['text']

    '''os.system("youtube-dl " + youtube_url)

    p = subprocess.Popen("ls -T | head -1", stdout=subprocess.PIPE, shell=True)
    (filename, err) = p.communicate()

    filename = filename.replace(" ", "\ ")
    filename = filename.replace("\n", "")
    filename_parsed = filename.replace("\ ", "_")
    filename_parsed = filename_parsed.replace("\n", "")

    # print "mv " + filename + " " + filename_parsed
    os.system("mv " + filename + " " + filename_parsed)

    os.system("ls -T | head -1")

    output_file = filename_parsed[0:len(filename_parsed) - 4] + ".mp3"
    os.system("ffmpeg -i " + filename_parsed + " -f mp3 " + output_file)
    
    # remember to delete original filename!'''

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port) # app.run()
