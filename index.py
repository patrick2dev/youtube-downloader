from flask import Flask, render_template, url_for, request
from pytube import YouTube

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html') 

@app.route("/api/youtube")
def api():
    yt = YouTube(request.args.get('url'))
    return {
        "title": yt.title,
        "thumbnail": yt.thumbnail_url,
        "author": yt.author,
        "views": yt.views,
        "source": {
            "download": yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().url,
            "resolution": yt.streams.filter(progressive=True).order_by('resolution').desc().first().resolution
        }
    }
