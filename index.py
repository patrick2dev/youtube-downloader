from flask import Flask, render_template, url_for, request
from pytube import YouTube
import pypugjs

app = Flask(__name__)
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')

def intWithCommas(x):
    if type(x) not in [type(0), type(0)]:
        raise TypeError("please int, please.")
    if x < 0:
        return '-' + intWithCommas(-x)
    result = ''
    while x >= 1000:
        x, r = divmod(x, 1000)
        result = ".%03d%s" % (r, result)
    return "%d%s" % (x, result)

@app.route("/")
def index():
    return render_template('index.pug')

@app.route("/api/youtube")
def api():
    yt = YouTube(request.args.get('url'))
    video = {
        "details": {
            "title": yt.title,
            "thumbnail": yt.thumbnail_url,
            "author": yt.author,
            "views": intWithCommas(yt.views),
        },
        "sources": []
    }
    sources = yt.streams.filter(progressive="true")
    for v in sources:
        video['sources'].append({
            "download": v.url,
            "resolution": v.resolution
        })
    return video
