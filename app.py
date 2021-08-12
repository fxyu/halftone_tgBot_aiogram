from flask import Flask
from flask import render_template
from flask_thumbnails import Thumbnail

app = Flask(__name__)
app.config['THUMBNAIL_MEDIA_ROOT'] = '/Users/felix/Project/tg_bot_test/data/'
app.config['THUMBNAIL_MEDIA_URL'] =  '/Users/felix/Project/tg_bot_test/media/'
thumb = Thumbnail(app)

@app.route('/')
def index_page():
    return render_template('index.html') 
