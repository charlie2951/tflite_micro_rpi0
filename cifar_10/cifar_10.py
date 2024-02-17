import numpy as np
import tflite_micro_runtime.interpreter as tf
labels = '''airplane automobile bird cat deerdog frog horseship truck'''.split()
# Initialize the TFLite interpreter
interpreter = tf.Interpreter(model_path="cifar_10.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()[0]
output_details = interpreter.get_output_details()[0]
#Read image
# Imports PIL module
from PIL import Image
# open method used to open different extension image file
im = Image.open("bird1.jpg")
new_image = im.resize((32, 32))
x_test=np.array(new_image)
x_test = x_test/255
# Invoke the interpreter
interpreter.set_tensor(input_details["index"], [x_test.astype(np.float32)])
interpreter.invoke()
y_pred1 = interpreter.get_tensor(output_details["index"])[0]
# save the predicted label
predicted_label1 = labels[y_pred1.argmax()]
print("Predicted label is:",predicted_label1)
