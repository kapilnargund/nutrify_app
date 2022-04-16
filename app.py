# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 22:34:20 2020
@author: Krish Naik
"""

from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np

# Keras
from backend.model import load_food_model, predict_class

# Flask utils
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
#from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

# # Model saved with Keras model.save()
# MODEL_PATH ='model_vgg19.h5'

# # Load your trained model
# model = load_model(MODEL_PATH)


food_model = load_food_model()


def model_predict(img_path):
    preds = predict_class(food_model, img_path)
    
    return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path)
        result=preds
        return result
    return None


if __name__ == '__main__':
    app.run(debug=True, port = 3001)
