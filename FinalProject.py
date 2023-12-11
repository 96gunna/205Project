from flask import Flask, render_template, request, flash, redirect, url_for
from transformationFunctions import scaling_fewer_pixels, scaling_up
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
    random_example = shuffled_ids[random.randint(0, len(shuffled_ids) - 1)]
    return render_template('examples.html',
                           random_example=random_example)


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        filter_type = request.form.get('filter')
        additional_filter_type = request.form.get('additional_filter')
        uploaded_image_path = os.path.join(app.config['UPLOAD_FOLDER'], "abac-rule-summary.png")
        # "/uploads/abac-rule-summary.png"  # Replace with the actual path

        if additional_filter_type == 'scaling_fewer_pixels':
            transformed_image_path = scaling_fewer_pixels(uploaded_image_path)
        elif additional_filter_type == 'scaling_up':
            transformed_image_path = scaling_up(uploaded_image_path)
        else:
            transformed_image_path = None

        return render_template('edit.html', transformed_image_path=transformed_image_path)

    return render_template('edit.html')


if __name__ == '__main__':
    app.run(debug=True)
