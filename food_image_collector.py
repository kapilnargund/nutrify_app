import PIL
import streamlit as st
import datetime
import os, requests, json
import uuid

from PIL import Image
from streamlit.uploaded_file_manager import UploadedFile

# from save_to_gsheets import append_values_to_gsheet
# from utils import create_unique_filename, upload_blob
from rich import pretty, print, traceback

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}

pretty.install()
traceback.install()

# Get filename for image upload source in database
IMAGE_UPLOAD_SOURCE = str(os.path.basename(__file__))

st.title("Nutrify Image Collection 🍔👁")
st.write(
    "Upload or take a photo of your food and help build the world's biggest \
        food image database!"
)

# Store image upload ID as key, this will be changed once image is uploaded
if "upload_key" not in st.session_state:
    st.session_state["upload_key"] = str(uuid.uuid4())

uploaded_image = st.file_uploader(
    label="Upload an image of food",
    type=["png", "jpeg", "jpg"],
    help="Tip: if you're on a mobile device you can also take a photo",
    key=st.session_state["upload_key"],  # set the key for the uploaded file
)


def display_image(img: UploadedFile) -> PIL.Image:
    """
    Displays an image if the image exists.
    """
    displayed_image = None
    if img is not None:
        # Show the image
        img = Image.open(img)
        print("Displaying image...")
        print(img.height, img.width)
        displayed_image = st.image(img, use_column_width="auto")
    return img, displayed_image


image, displayed_image = display_image(uploaded_image)

# Create image label form to submit
st.write("## Image details")
with st.form(key="image_metadata_submit_form", clear_on_submit=True):
    # Submit button + logic
    submit_button = st.form_submit_button(
        label="Upload image",
        help="Click to upload your image and label to Nutrify servers",
    )

    if submit_button:
        if uploaded_image is None:
            st.error("Please upload an image")
        else:
            # response = requests.get("http://127.0.01:3000/register")
            # # print(response.json())
            # print(response.text)


            img = open(IMAGE_UPLOAD_SOURCE, 'rb').read()
            print(img)
            response = requests.post("http://127.0.01:3000/register-new", data=img, headers=headers)
            print(response.text)