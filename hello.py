from flask import Flask
from flask import request
from flask import render_template
from pytinysong.request import TinySongRequest
import os
import subprocess
import boto

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("my_form.html")

@app.route('/', methods=['POST'])
def my_form_post():
    youtube_url = request.form['text']

    os.system("cd #{RAILS_ROOT}/tmp/")

    p = subprocess.Popen("youtube-dl -e --get-title " + youtube_url, stdout=subprocess.PIPE, shell=True)
    (youtube_title, err) = p.communicate()

    # hard-coding a beyonce file for debugging
    # https://www.youtube.com/watch?v=pZ12_E5R3qc

    os.system("youtube-dl " + youtube_url) 

    # https://www.youtube.com/watch?v=Blfi00qCQs4 // battles
    os.system("ls > files.txt") 

    f = open('files.txt', 'r')
    
    while True:
        filename = f.readline()
        
        if (".mp4" in filename):
            break

        if (filename == ""):
            break

    f.close()

    # load metadata using pytinysong
    song = TinySongRequest(api_key='0a3a9ca81670447ae6e735a80f17070e')
    results = song.request_metadata(youtube_title)

    artist_name = results.artist_name
    song_name = results.song_name
    album_name = results.album_name

    # do i need this?
    filename = filename.replace(" ", "\ ")
    filename = filename.replace("\n", "")
    filename_parsed = filename.replace("\ ", "_")
    filename_parsed = filename_parsed.replace("\n", "")

    os.system("mv " + filename + " " + filename_parsed)

    mp3_file = filename_parsed[0:len(filename_parsed) - 4] + ".mp3"

    # build string

    os.system("chmod 755 /app/.heroku/vendor/ffmpeg")

    ffmpeg = "/app/.heroku/vendor/ffmpeg -y -i " + filename_parsed # issue: i want a prettier .mp3 file
    ffmpeg = ffmpeg + " -metadata title=" +  "\"" + song_name   + "\"" + " "
    ffmpeg = ffmpeg + " -metadata artist=" + "\"" + artist_name + "\"" + " "
    ffmpeg = ffmpeg + " -metadata album=" + "\""  + album_name  + "\"" + " " + mp3_file

    os.system(ffmpeg)

    p = subprocess.Popen("ls -l", stdout=subprocess.PIPE, shell=True)
    (final_download, err) = p.communicate()

    # upload to aws s3
    AWS_ACCESS_KEY_ID = 'AKIAJ6GQTHMXX4E34K4Q'
    AWS_SECRET_ACCESS_KEY = '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'

    conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
            AWS_SECRET_ACCESS_KEY)
    
    bucket = conn.get_bucket('downloader-proj-assets')

    # testfile = "Battles_-_Tras_3-Blfi00qCQs4.mp3" #mp3_file
    testfile = mp3_file

    return final_download
'''
    import sys
    def percent_cb(complete, total):
        sys.stdout.write('.')
        sys.stdout.flush()

    from boto.s3.key import Key
    k = Key(bucket)
    k.key = testfile
    k.set_contents_from_filename(testfile,
        cb=percent_cb, num_cb=10)

    k.set_acl('public-read')

    final_download = "https://s3.amazonaws.com/downloader-proj-assets/" + k.key
    return render_template("my_form_2.html", final_download = final_download) #final_download = amazon link'''

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port) # app.run()
