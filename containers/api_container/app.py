from connexion import FlaskApp
import base64
import numpy as np
import cv2
import os
from utils.model import NN
from pathlib import Path

trained_model_location = 'model'
model = NN.load(trained_model_location)

def solve(image):
    nparr = np.fromstring(base64.b64decode(image), np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return model.solve(image)

def version():
    return "version: 1.0.0", 200

app = FlaskApp(__name__, specification_dir='./')
app.add_api('openapi.yaml')

if __name__ == '__main__':
    app.run(f"{Path(__file__).stem}:app", port=int(os.environ.get('PORT')), host="0.0.0.0")
