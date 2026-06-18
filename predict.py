import os
import numpy as np
from tensorflow.keras.models import load_model

BASE_DIR = os.path.dirname(os.path.abspath(**file**))

MODEL_PATH = os.path.join(
BASE_DIR,
"model",
"fingerprint_blood_group_model_1.keras"
)

blood_groups = [
'A+',
'A-',
'AB+',
'AB-',
'B+',
'B-',
'O+',
'O-'
]

model = load_model(MODEL_PATH)

def predict_blood_group(processed_image):
prediction = model.predict(processed_image)

```
return blood_groups[np.argmax(prediction)]
```
