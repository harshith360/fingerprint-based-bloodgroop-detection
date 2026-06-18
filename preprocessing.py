import cv2
import numpy as np

def preprocess_fingerprint(image_path):
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

```
if image is None:
    raise ValueError("Unable to read fingerprint image")

resized_image = cv2.resize(image, (224, 224))

processed_image = resized_image / 255.0
processed_image = np.expand_dims(processed_image, axis=-1)
processed_image = np.expand_dims(processed_image, axis=0)

return image, processed_image
```
