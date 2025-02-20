import json
CLASS_NAMES = ["a", "b", "c"]
# res = json.dumps({
#     "model": "MODEL_NAME",
#     "predictions": {
#         "filename": "photo1.jpg",
#         "scores": { clas:0.2 for i, clas in enumerate(CLASS_NAMES) }
#     }
# })
# print(res)
# print(res.encode())
# exit()
import numpy as np
import tensorflow.lite as tflite  # Use `import tflite_runtime.interpreter as tflite` if using tflite-runtime

# Load the TFLite model
interpreter = tflite.Interpreter(model_path="models/vgg16-original-adam.tflite")
interpreter.allocate_tensors()  # Allocate memory for the model

# Get input/output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Create a sample input tensor (adjust shape accordingly)
input_shape = input_details[0]['shape']
print(input_shape)
# exit()
input_data = np.random.rand(*input_shape).astype(np.float32)  # Replace with real input data

# Set input tensor
interpreter.set_tensor(input_details[0]['index'], input_data)

# Run inference
interpreter.invoke()

# Get the output
output_data = interpreter.get_tensor(output_details[0]['index'])
output_data = output_data.tolist()
print("Model Output:", output_data)
res = json.dumps({
    "model": "MODEL_NAME",
    "predictions": {
        "filename": "photo1.jpg",
        "scores": { clas:output_data[0][i] for i, clas in enumerate(CLASS_NAMES) }
    }
})
print(res)
print(res.encode())