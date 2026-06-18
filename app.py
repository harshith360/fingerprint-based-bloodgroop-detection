from flask import Flask, render_template, jsonify
import subprocess
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import time
import base64
import os

app = Flask(__name__)

# Load the trained model (expects grayscale input shape: (224, 224, 1))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "fingerprint_blood_group_model_1.keras"
)

model = load_model(MODEL_PATH) 
blood_groups = ['A+', 'A-', 'AB+', 'AB-', 'B+', 'B-', 'O+', 'O-']

# Paths
cpp_exe_path = r"C:\Users\ASUS\source\repos\SecugenConnect\x64\Debug\SecugenConnect.exe"
captured_image_path = r"C:\Users\ASUS\source\repos\SecugenConnect\fingerprint\fingerprint.bmp"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict')
def predict():
    try:
        # Run the fingerprint capture executable
        subprocess.run([cpp_exe_path], timeout=10)
        time.sleep(1)  # Give some time for the image to be saved

        # Check if the fingerprint image exists
        if not os.path.exists(captured_image_path):
            return jsonify({'status': "Image not found", 'prediction': None, 'image_data': None})

        # Load image as GRAYSCALE
        image = cv2.imread(captured_image_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            return jsonify({'status': "Error reading image", 'prediction': None, 'image_data': None})

        # Preprocess the image
        resized_image = cv2.resize(image, (224, 224))
        processed_image = resized_image / 255.0  # Normalize
        processed_image = np.expand_dims(processed_image, axis=-1)  # (224, 224, 1)
        processed_image = np.expand_dims(processed_image, axis=0)   # (1, 224, 224, 1)

        # Predict
        prediction = model.predict(processed_image)
        predicted_label = blood_groups[np.argmax(prediction)]

        # Convert original image (grayscale) to base64 for web display
        color_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        _, buffer = cv2.imencode('.bmp', color_image)
        encoded_image = base64.b64encode(buffer).decode('utf-8')
        image_data = f"data:image/bmp;base64,{encoded_image}"

        return jsonify({
            'status': "Fingerprint captured!",
            'prediction': predicted_label,
            'image_data': image_data
        })

    except Exception as e:
        return jsonify({'status': f"Error: {str(e)}", 'prediction': None, 'image_data': None})

if __name__ == '__main__':
    app.run(debug=True)