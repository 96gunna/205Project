from flask import Flask, render_template, request, flash, redirect, url_for, session
from transformationFunctions import scaling_fewer_pixels, scaling_up
from functions import Grayscale, Sepia, Negative, Thumbnail
from flask_bootstrap import Bootstrap5
from PIL import Image
from io import BytesIO
from example_ids import example_ids
import random
import os
from flask import send_from_directory
from functions import Sepia, Grayscale, Negative, Thumbnail


""" CST 205
Second Image
Users can upload and image to then apply various filters or transformations to.
Matthew Custodio, Mariana Duran, Alfredo Gunn, Ryan Mauvais, Sydney Stalker
12/13/2323
"""

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
    random_example = shuffled_ids[random.randint(0, len(shuffled_ids) - 1)]
    pathway = os.path.join("static","example_images",random_example+".jpg")
    transformed_image_path1 = Grayscale(pathway)  
    transformed_image_path2 = Sepia(pathway)  
    transformed_image_path3 = Negative(pathway) 
    
    
    
    return render_template('examples.html',
                           random_example=random_example, transformed_image_path1 = transformed_image_path1, transformed_image_path2= transformed_image_path2, transformed_image_path3 = transformed_image_path3)
            
   


@app.route('/edit/<name>', methods=['GET', 'POST'])
def edit(name):
    if request.method == 'POST':
        filter_type = request.form.get('filter')
        additional_filter_type = request.form.get('additional_filter')
        uploaded_image_path = os.path.join(app.config['UPLOAD_FOLDER'], name)
        # "/uploads/abac-rule-summary.png"  # Replace with the actual path

        if filter_type == 'grayscale':
            transformed_image_path = Grayscale(uploaded_image_path)  # Assuming you want to apply Grayscale directly
        elif filter_type == 'sepia':
            transformed_image_path = Sepia(uploaded_image_path)  # Assuming you want to apply Sepia directly
        elif filter_type == 'negative':
            transformed_image_path = Negative(uploaded_image_path)  # Assuming you want to apply Negative directly'
        elif filter_type == 'thumbnail':
            transformed_image_path = Thumbnail(uploaded_image_path)
        # Add other filter conditions as needed

        elif additional_filter_type == 'scaling_fewer_pixels':
            transformed_image_path = scaling_fewer_pixels(uploaded_image_path)
        elif additional_filter_type == 'scaling_up':
            transformed_image_path = scaling_up(uploaded_image_path)
        else:
            transformed_image_path = None

        return render_template('edit.html', transformed_image_path=transformed_image_path)

    return render_template('edit.html')


if __name__ == '__main__':
    app.run(debug=True)
