from flask import Flask
from flask import render_template
import opentimelineio as otio


app = Flask(__name__)


@app.route("/")
def upload_form():
    return render_template("index.html")

@app.route('/', methods = ['POST'])
def upload_file():
    if request.method == 'POST':
        
        return 'file uploaded successfully'

        