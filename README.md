\# Fingerprint-Based Blood Group Prediction



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



