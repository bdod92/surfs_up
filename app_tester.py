#Flask script to use with the surfs_up weather investigation

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'
