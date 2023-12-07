from flask import Flask, render_template, request, flash, redirect, url_for
from flask_bootstrap import Bootstrap5
from PIL import Image
from io import BytesIO
from example_ids import example_ids
import random
import os
from flask import send_from_directory

UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
Bootstrap5(app)

app.config['SECRET_KEY'] = 'lilboi'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def user_upload():
    file = request.files['file']

    if file:
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return render_template('upload.html', image_path=filename)
    
    flash('No file uploaded.')
    return redirect(url_for('index'))

@app.route('/uploads/<filename>')
def serve_uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/examples', methods=('GET', 'POST'))
def show_examples():
    shuffled_ids = example_ids
    random.shuffle(shuffled_ids)
    random_example = shuffled_ids[random.randint(0, len(shuffled_ids)-1)]
    return render_template('examples.html',
                           random_example=random_example)
