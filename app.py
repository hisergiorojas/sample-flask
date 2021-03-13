from flask import Flask
from flask import render_template
import opentimelineio as otio


app = Flask(__name__)


@app.route("/")
def upload_file():
    return render_template("index.html")

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file2():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'