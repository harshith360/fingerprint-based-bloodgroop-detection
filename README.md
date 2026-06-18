# Fingerprint-Based Blood Group Detection

## Overview

Fingerprint-Based Blood Group Detection is a deep learning-based system designed to predict a person's blood group using fingerprint images. The project combines biometric fingerprint analysis, image processing techniques, and Convolutional Neural Networks (CNNs) to explore a non-invasive approach to blood group prediction.

The application captures a fingerprint image, performs preprocessing, extracts meaningful features, and classifies the fingerprint into one of the eight blood groups:

* A+
* A-
* B+
* B-
* AB+
* AB-
* O+
* O-

---

## Key Features

* Fingerprint image acquisition using a biometric fingerprint scanner
* Image preprocessing and enhancement using OpenCV
* Blood group prediction using a deep learning model
* Interactive web-based interface built with Flask
* Real-time prediction and result visualization
* Support for all ABO and Rh blood group classifications

---

## Technology Stack

### Programming Language

* Python

### Frameworks and Libraries

* Flask
* TensorFlow
* Keras
* OpenCV
* NumPy

### Frontend

* HTML
* CSS
* JavaScript

### Development Tools

* Visual Studio Code
* Git
* GitHub

---

## System Workflow

The application follows the workflow below:

1. Capture fingerprint image using the biometric scanner.
2. Preprocess the captured image for improved quality and consistency.
3. Extract relevant fingerprint features.
4. Feed the processed image into the trained CNN model.
5. Predict and display the corresponding blood group.

---

## Project Structure

```text
Fingerprint-Blood-Group-Detection/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
├── screenshots/
│
├── docs/
│
└── model/
```

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/harshith360/fingerprint-based-bloodgroop-detection.git
cd fingerprint-based-bloodgroop-detection
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python app.py
```

### 4. Open the Application

Open your browser and navigate to:

```text
http://127.0.0.1:5000
```

---

## Model Information

The trained model file is not included in this repository due to GitHub file size limitations.

To use the application:

1. Train your own model or obtain a compatible trained model.
2. Place the model file inside the `model` directory.
3. Update the model path in `app.py` if necessary.
4. Run the application as described above.

---

## Screenshots

### Application Home Page

*(Add screenshot here)*

### Fingerprint Capture

*(Add screenshot here)*

### Prediction Result

*(Add screenshot here)*

---

## Results

The system demonstrates the integration of biometric fingerprint acquisition with deep learning-based classification. The project successfully performs:

* Fingerprint capture
* Image preprocessing
* Feature extraction
* Blood group prediction
* Real-time result visualization

---

## Future Enhancements

The project can be further improved through:

* Expansion of the training dataset
* Improved image preprocessing techniques
* Advanced deep learning architectures
* Higher prediction accuracy through hyperparameter optimization
* Cloud deployment for remote access
* Mobile application integration
* Healthcare and diagnostic system integration

---

## Limitations

* Prediction accuracy depends heavily on dataset quality and size.
* The system requires a compatible fingerprint scanner for image acquisition.
* The trained model is not distributed with the repository.
* This project is intended for academic and research purposes.


---

## License

This project is intended for educational, research, and academic purposes.
