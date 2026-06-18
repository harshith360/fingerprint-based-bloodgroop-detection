Fingerprint-Based Blood Group Detection

Overview

Fingerprint-Based Blood Group Detection is a deep learning-based system that predicts a person's blood group using fingerprint images. The project combines biometric fingerprint analysis, image processing, and Convolutional Neural Networks (CNNs) to provide a non-invasive approach for blood group prediction.

The system captures a fingerprint image, preprocesses it, extracts meaningful features, and predicts one of the eight blood groups:

A+
A-
B+
B-
AB+
AB-
O+
O-

Features
Fingerprint image acquisition using biometric scanner

Image preprocessing with OpenCV

Deep learning-based blood group prediction

Flask web application interface

Real-time prediction and result display

Support for all ABO and Rh blood groups

Technologies Used
Python

TensorFlow

Keras

OpenCV

NumPy

Flask

HTML

CSS

System Architecture
Fingerprint Acquisition

Image Preprocessing

Feature Extraction

CNN-Based Classification

Blood Group Prediction

Project Structure
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
└── model/
Installation
Clone the repository:

git clone https://github.com/harshith360/fingerprint-based-bloodgroop-detection.git
cd fingerprint-based-bloodgroop-detection
Install dependencies:

pip install -r requirements.txt
Run the application:

python app.py
Open your browser and visit:

http://127.0.0.1:5000
Model Information
The trained model file is not included in this repository because of GitHub's file size limitations.

To use the project:

Train your own model using the dataset.

Place the trained .keras model inside the model folder.

Update the model path in app.py.

Screenshots
User Interface
(Add screenshots here)

Prediction Results
(Add screenshots here)ngerprint-Based Blood Group Prediction



\## Overview



This project is a Flask-based web application that captures fingerprint images using a SecuGen fingerprint scanner and predicts blood groups using a deep learning model.



\## Features



\* Fingerprint capture using SecuGen scanner

\* Image preprocessing with OpenCV

\* Blood group prediction using TensorFlow/Keras

\* Web-based user interface using Flask

\* Real-time prediction display



\## Tech Stack



\* Python

\* Flask

\* TensorFlow / Keras

\* OpenCV

\* NumPy

\* HTML, CSS, JavaScript



\## Project Structure



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

├── model/

│   └── fingerprint\_blood\_group\_model\_1.keras

│

└── screenshots/

```



\## How to Run



1\. Install dependencies



```bash

pip install -r requirements.txt

```



2\. Run the application



```bash

python app.py

```



3\. Open your browser and visit:



```text

http://127.0.0.1:5000

```



\## Note



This project was developed as a machine learning research project exploring fingerprint-based blood group prediction using a custom dataset.



The trained model file is not included in this repository due to GitHub file size limitations.



