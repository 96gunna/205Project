from flask import Flask, render_template, flash, redirect, url_for
from flask_bootstrap import Bootstrap5
from PIL import Image
import random

app = Flask(__name__)
Bootstrap5(app)

app.config['SECRET_KEY'] = 'lilboi'


@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')
