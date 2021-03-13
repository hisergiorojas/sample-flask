from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import opentimelineio as otio

app = Flask(__name__)


@app.route("/")
def upload_form():
    return render_template("index.html")

@app.route('/', methods = ['POST'])
def upload_file():
    if request.method == 'POST':
        
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'
        