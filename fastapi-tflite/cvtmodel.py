import tensorflow as tf

model = tf.keras.applications.VGG16(
    include_top=True,
    weights=None,
    classes=3,
    classifier_activation='softmax'
)

model.load_weights("models/vgg16-original-adam.weights.h5")
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()

with open("models/vgg16-original-adam.tflite", "wb") as f:
    f.write(tflite_model)
    f.close()
