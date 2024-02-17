# MNIST Digit Classification on Pi-Zero using Tensorflow-Lite
![mnist-3 0 1](https://github.com/charlie2951/tflite_micro_rpi0/assets/90516512/acbadc1d-62df-440b-801c-725a7dd72d1f)
<br>
MNIST dataset contain GRAYscale image for handwritten digits (from 0 to 9) with 28 x 28 pixel image size.<br>
A fully connected Dense layer model is trained on tensorflow and model is converted to TFLITE format. Then the inference 
was performed on Pi-Zero system with TFLITE-MICRO runtime. The model performs well for both sample test images and real
handwritten images. <br>
**Note** that for real handwritten image, you need to rescale the camera captured image by 28 x 28 and also the image needs to be converted into GrayScale. 
Then the image pixels was inverted (in grayscale black-0 and white-255 and in training data, images are written on White color on black background.). All these steps was done easily using OpenCV.
