# imgur-newest.py

from flask import Flask
from flask import render_template
import requests
import json
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

app = Flask(__name__)
imgurClientId = 'Client-ID bef23334d5728ff'

@app.route('/', methods=['GET'])
def index():
    '''
    serve up the HTML page
    '''
    return app.send_static_file('index.html')

@app.route('/app.js', methods=['GET'])
def jsApp():
    '''
    lets the frontend load the JS app
    '''
    return app.send_static_file('app.js')

@app.route('/getimage', methods=['GET'])
def getImage():
    '''
    gets the latest image from user-sub
    '''
    headers = {
        'Authorization' : imgurClientId
    }
    req = requests.get('https://api.imgur.com/3/gallery/user/time/0', headers=headers, verify=False)
    return req.text

@app.route('/getimageuri/<id>', methods=['GET'])
def getImageUri(id):
    '''
    gets the uri of an image
    '''
    headers = {
        'Authorization' : imgurClientId
    }
    req = requests.get('https://api.imgur.com/3/image/' + id, headers=headers, verify=False)
    return req.text

# debug
app.run(host='0.0.0.0', port=5000)

#EOF