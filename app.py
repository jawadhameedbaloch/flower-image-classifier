# app.py

import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image

st.set_page_config(
    page_title="Flower Classifier 🌸",  # Appears in browser tab
    page_icon="🌸",                     # Emoji OR path to image file
    layout="centered"
)

# Load model
model = tf.keras.models.load_model("flower_classifier.h5")

# Class names
class_names = ['dandelion', 'daisy', 'tulips', 'sunflowers', 'roses']

# App title
st.title("🌸 Flower Classifier")
st.write("Upload an image of a flower and I’ll tell you what it is!")

# Upload image
uploaded_file = st.file_uploader("Choose a .jpg or .png image", type=["jpg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Uploaded Image', use_container_width=True)

    # Preprocess
    image = image.resize((224, 224))
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions)]
    confidence = np.max(predictions) * 100

    # Output
    st.write(f"### 🧠 Prediction: {predicted_class}")
    st.write(f"### 🔍 Confidence: {confidence:.2f}%")

    

