import flask
from flask import Flask, render_template, request
from PIL import Image

from settings import *

app = Flask(__name__, template_folder='template')

@app.route('/')
def home():
    return "Hello World"

@app.route('/test')
def load_image(name=None):
    return render_template('index.html', name=name)

@app.route('/post_image', methods=['GET','POST'])
def send_image():
    image = request.files
    print(image, type(image))
    return 'Hello world!'

if __name__ == '__main__':
    app.run(debug=DEBUG)