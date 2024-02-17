#Run this script on Pi-Zero
import numpy as np
import tflite_micro_runtime.interpreter as tf
import cv2
# Initialize the TFLite interpreter
interpreter = tf.Interpreter(model_path="mnist_digit.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()[0]
output_details = interpreter.get_output_details()[0]
#Read image and transform and resizing using OpenCV
img=cv2.imread('0.png')
x_test = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
x_test = cv2.resize(x_test,(28,28))
#Invert the image because in MNIST dataset, digit pixels are white
x_test = cv2.bitwise_not(x_test)
x_test = x_test/255 #Normalize image data in between 0 and 1
#Apply input (here we are applying scaled input from test set)
#Later we shall go for live classification
# Invoke the interpreter
interpreter.set_tensor(input_details["index"], [x_test.astype(np.float32)])
interpreter.invoke()
y_pred = interpreter.get_tensor(output_details["index"])[0]
print(y_pred)
#set labels for output classes
labels = '''0 1 2 3 4 5 6 7 8 9'''.split()
# save the predicted label
predicted_label = labels[y_pred.argmax()]

# display the result
print("Predicted image label is:", predicted_label)

