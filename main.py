import os
import flask
from flask import Flask, render_template, request
from PIL import Image

from settings import *
from utils import get_string_from_image

app = Flask(__name__, template_folder='template')

@app.route('/')
def home():
    return "Hello World"

@app.route('/test')
def load_image(name=None):
    return render_template('index.html', name=name)

@app.route('/post_image', methods=['GET','POST'])
def send_image():
    request_image = request.files['imagefile'].stream
    img = Image.open(request_image)
    return get_string_from_image(img)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=DEBUG)