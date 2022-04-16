from flask import Flask, request
from flask_cors import CORS, cross_origin
import base64, os
from werkzeug.utils import secure_filename

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def index():
    return 'Web App with Python Flask!'

@app.route('/register', methods=['GET', 'POST'])
def register():
    return 'Hello from flask'
    
@app.route('/register-new', methods=['POST'])
@cross_origin()
def register_new():
    # photo = request.get_json()
    # print(photo)
    # photo_data = base64.b64decode(photo)
    
    # with open("compare.jpg", "wb") as file:
    #     file.write(photo_data)

    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

app.run(host='localhost', port=3000, debug = True)
