from flask import Flask, render_template, jsonify
import subprocess
import base64
import cv2
import os
import time

from preprocessing import preprocess_fingerprint
from predict import predict_blood_group

app = Flask(__name__)

cpp_exe_path = r"..."
captured_image_path = r"..."

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
        image, processed_image = preprocess_fingerprint(captured_image_path)

        predicted_label = predict_blood_group(processed_image)

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
