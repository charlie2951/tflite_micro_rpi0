#Inference for sine wave
#Model trained in Colab using Tensorflow and converted into TFLITE
import numpy as np
import tflite_micro_runtime.interpreter as tf
interpreter=tf.Interpreter(model_path='sine.tflite')
interpreter.allocate_tensors()
# Get input and output tensors.
input_details = interpreter.get_input_details()[0]
output_details = interpreter.get_output_details()[0]
# Test the model on random input data.
#input_shape = input_details[0]['shape']
#print(input_shape)
x_test = np.linspace(0,6.28,20).astype(np.float32)
x_test = x_test.reshape((x_test.size, 1))
x_test = x_test.astype(np.float32)
#Invoke the interpreter
y_pred = np.empty(x_test.size,dtype=output_details["dtype"])
for i in range(len(x_test)):
	interpreter.set_tensor(input_details['index'], [x_test[i]])
	interpreter.invoke()
	y_pred[i] = interpreter.get_tensor(output_details["index"])[0]
# The function `get_tensor()` returns a copy of the tensor data.
# Use `tensor()` in order to get a pointer to the tensor.
#calculate actual value
inp=np.linspace(0,6.28,20)
y_true = np.sin(inp).astype(np.float32)
print('Running Inference for Sine wave prediction....\n')
for i in range(len(y_true)):
	print("Actual val:",y_true[i])
	print("Predicted val:",y_pred[i])
	print("\n")


