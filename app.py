from flask import Flask, flash, request, redirect, render_template, send_file
from werkzeug.utils import secure_filename
import os
import opentimelineio as otio

app = Flask(__name__)


@app.route("/")
def upload_form():
    response = request.get('.https://api.pandascore.co/matches/upcoming?token=1nW7K4Ys0yeOe2Uqq4yTIUjr_szzLxuR1-dLhPDIgVxkfbCkHrQ')
    print(response.json())
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