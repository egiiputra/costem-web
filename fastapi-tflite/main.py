from typing import List
from fastapi import (
    FastAPI, 
    UploadFile, 
    Response, 
    status
)

import numpy as np
import cv2
from ai_edge_litert.interpreter import Interpreter

BATCH_SIZE = 10

CLASS_NAMES = ['sehat', 'giberella', 'anthracnose']

MODEL_NAME = "vgg16-original-adam"

# Load the TFLite model
interpreter = Interpreter(model_path=f"models/{MODEL_NAME}.tflite")
interpreter.allocate_tensors()  # Allocate memory for the model

# Get input/output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

app = FastAPI()

@app.get("/")
def read_root():
    return "Hello world!"

@app.post("/predicts")
async def predicts(images: List[UploadFile], response: Response):
    if len(images) > BATCH_SIZE:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return { 'message' : 'To many images to inference' }

    # Check MIME Type make sure that file is image
    for image in images:
        if image.content_type not in ('image/jpeg', 'image/png'):
            response.status_code = status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
            return { 'message' : 'Just can receive image file type'}

    predictions = []
    for i, image in enumerate(images):
        tmp = cv2.imdecode(
            np.frombuffer(await image.read(), dtype=np.uint8),
            cv2.IMREAD_COLOR_RGB
        )
        tmp = np.array(
            object=[ cv2.resize(tmp, (224, 224)) / 255 ],
            dtype=np.float32
        )

        interpreter.set_tensor(input_details[0]['index'], tmp)
        # Run inference
        interpreter.invoke()
        # Get the output
        output_data = interpreter.get_tensor(output_details[0]['index'])
        output_data = output_data.tolist()

        predictions.append({ 
            "file_name": images[i].filename,
            "scores": {clas:output_data[0][i] for i, clas in enumerate(CLASS_NAMES) }
        })

    return {
        "model": MODEL_NAME,
        "predictions": predictions
    }
