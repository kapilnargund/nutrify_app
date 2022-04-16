import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
import os
import tensorflow.keras.backend
from tensorflow.keras.preprocessing import image
from backend.classes import foods_sorted

def load_food_model():
    tensorflow.keras.backend.clear_session()
    model_best = load_model('/home/kapil/Documents/open_cv/nutrify/models/best_model_101class.hdf5',compile = False)
    return model_best

def predict_class(model, img, show = True):

    img = image.load_img(img, target_size=(200, 200))
    img = image.img_to_array(img)                    
    img = np.expand_dims(img, axis=0)         
    img = img / 255.                                      

    pred = model.predict(img)
    index = np.argmax(pred)
    foods_sorted.sort()
    pred_value = foods_sorted[index]
    
    return pred_value

# image_path = '../images'
# images = os.path.join(image_path, 'chocolate_mousse.jpg')

# model_best = load_food_model()
# predict_class(model_best, images, True)