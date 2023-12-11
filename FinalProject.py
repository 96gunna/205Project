from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_bootstrap import Bootstrap5
from PIL import Image
from io import BytesIO
from example_ids import example_ids
import random
import os
from flask import send_from_directory
from functions import Sepia, Grayscale, Negative, Thumbnail

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
        session['uploaded_file'] = filename
        return render_template('upload.html', image_path=filename)
    
    flash('No file uploaded.')
    return redirect(url_for('index'))

@app.route('/apply_filter', methods=['POST'])
def apply_filter():
    filter_type = request.form.get('filter')
    filename = session.get('uploaded_file')
    if filename:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        processed_image_path = apply_filter_to_image(file_path, filter_type)
        return render_template('display.html', image_path=processed_image_path)
    flash('No image to apply filter.')
    return redirect(url_for('index'))

def apply_filter_to_image(image_path, filter_type):
    # Map filter types to function calls
    filter_functions = {
        'grayscale': Grayscale,
        'sepia': Sepia,
        'negative': Negative,
        'thumbnail':Thumbnail,
    }
    if filter_type in filter_functions:
        return filter_functions[filter_type](image_path)
    return image_path

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
