from flask import Flask, flash, request, redirect, render_template, send_file
from werkzeug.utils import secure_filename
import os
import requests
import opentimelineio as otio

app = Flask(__name__)
app.secret_key = 'secret key' # for encrypting the session

# It will allow below 16MB contents only, you can change it
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

path = os.getcwd()

# file upload
UPLOAD_FOLDER = os.path.join(path, 'uploads')

if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in  ALLOWED_EXTENSIONS


@app.route("/")
def upload_form(): 
    return render_template("upload.html")

@app.route('/', methods = ['POST'])
def upload_file():
    if request.method == 'POST':       
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('No file selected for uplloading')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully uploaded')
            return redirect('/')
        else:
            flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
            return redirect(request.url)

       # f = request.files['file']
       # f.save(secure_filename(f.filename))

        #filename = os.path.splitext(f.filename)[0]
        #timeline = otio.adapters.read_from_file(f.filename)
        #download_filename = filename + '.otio'
       
        #otio.adapters.write_to_file(timeline, download_filename)

        #return send_file(download_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)