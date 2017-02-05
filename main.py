# imgur-newest.py

from flask import flask
import requests
import json

app = Flask(__name__)
imgurClientId = 'Client-ID bef23334d5728ff'


@app.route('/')
def index():
    '''
    serve up the HTML page
    '''
    return app.send_static_file('index.html')

@app.route('/getimage')
def getImage():
    '''
    gets the latest image from user-sub
    '''
    headers = {
        'Authorization' : imgurClientId
    }
    req = requsts.get('https://api.imgur.com/3/gallery/user/time/0?showViral=false&perPage=1')
    
