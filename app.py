from flask import Flask, request
import db

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/photos.json')
def index():
    return db.all_photos()

@app.route("/photos.json", methods=["POST"])
def create():
    name = request.form.get("name")
    width = request.form.get("width")
    height = request.form.get("height")
    return db.create_photo(name, width, height)