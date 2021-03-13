from flask import Flask, flash, request, redirect, render_template, send_file
from werkzeug.utils import secure_filename
import os
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

        filename = os.path.splitext(f.filename)[0]
        timeline = otio.adapters.read_from_file(f.filename)
        download_filename = filename + '.otio'
       
        otio.adapters.write_to_file(timeline, download_filename)

        return send_file(download_filename, as_attachment=True)