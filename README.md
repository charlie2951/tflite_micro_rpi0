# Tensorflow-Lite Runtime and tested designs for Raspberry Pi Zero/Zero-W (ARMV6 architecture)
Running Tensorflow Lite runtime in Python on Raspberry Pi Zero and Zero W running Raspberrian OS Bullseye Python V 3.9  <br>
## Install Prequisite packages <br>
**1. Installing OpenCV on Raspberry Pi Zero/Zero W** <br>
*Install Required libraries required by OpenCV*
```
sudo apt install libxrender1 libx265-192 libxi6 ocl-icd-libopencl1 libxcb-render0 libtwolame0 libwebpmux3 libvorbisenc2 libsrt1.4-gnutls libgraphite2-3 libva-x11-2 libwayland-egl1 libgme0 libmp3lame0 libcairo-gobject2 libspeex1 libavcodec58 libswresample3 libdav1d4 libdrm2 libxvidcore4 libtheora0 libxfixes3 libvpx6 libvdpau1 libwayland-client0 libharfbuzz0b libatlas3-base libzmq5 libudfread0 libssh-gcrypt-4 libmpg123-0 libaom0 libgdk-pixbuf-2.0-0 libogg0 libpangocairo-1.0-0 libxcb-shm0 libbluray2 librabbitmq4 libpgm-5.3-0 libopenmpt0 libpangoft2-1.0-0 libatspi2.0-0 libwayland-cursor0 libcodec2-0.9 libxrandr2 libxinerama1 libxcomposite1 libgtk-3-0 libxkbcommon0 libva-drm2 libgsm1 librsvg2-2 libopenjp2-7 libxdamage1 libpixman-1-0 libswscale5 libavutil56 libsodium23 libcairo2 libatk1.0-0 libpango-1.0-0 libthai0 libxcursor1 libavformat58 libopus0 libdatrie1 libvorbis0a libsoxr0 libva2 libatk-bridge2.0-0 libzvbi0 libshine3 libx264-160 libvorbisfile3 libepoxy0 libchromaprint1 libwavpack1 libgfortran5 libnorm1 libsnappy1v5
```

Then install OpenCV using pip:
```
  pip3 install opencv-python==4.6.0.66
```
**2. Installing TF-LITE-MICRO runtime packages** <br>
Related packages and instructions are collected from [here](https://github.com/driedler/tflite_micro_runtime). <br>
For the installation of pre-compiled and pre-build wheel, download/clone this repo and navigate to the main directory. Then use pip command to install the tflite-micro runtime. Depending upon your Python version use appropriate wheel file (e.g. cp37 for Python 3.7 and cp39 for Python 3.9)<br>
```
pip install tflite_micro_runtime-1.2.2-cp39-cp39-linux_armv6l.whl
```
This will install Tensorflow-Lite-micro runtime into your system. Note that Numpy is required for this and it will be automatically downloaded during installation. If you do not want to install numpy then run the pip command along with *--no-deps* flag.  <br>
Note that basic functionalities and API for Tensorflow-Lite and Tensorflow-Lite-Micro (mainly targetted for Microcontrollers) are similar. In case of tflite-micro, some advanced models and functions are not included. Refer to the official documentation of Tensorflow for this.  TFLITE MICRO is are mainly for tiny microcontrollers with little memory footprints whereas TFLITE is extensively used in Android/IOS apps. RPI-0 belongs to ARM-6 architecture, the default Neural network lib from Tensorflow source code is not optimized. The tflite-micro runtime package is compiled using ARM CMSIS NN library which is optimized for armv6 architecture. <br>
This repo contain some pre-trained models **(CIFAR-10 image classification, MNIST Digit identifier)** converted into TFLITE format and accessable using the tflite-micro runtime. Check the individual directory for the descriptions and source code. These code has been tested on RPI-0 with Raspberrian Bullseye OS with Python V3.9 and they are working properly. These codes are also tested for ***real time input data taken from Raspberry-Pi camera module.*** <br>

## List of Tested Projects using TFLITE-MICRO Runtime <br>
These models are trained on desktop.Google Colab and trained model is converted to TFLITE format. Then, these models are transferred into Raspberry Pi using sftp and Inference was performed. <br>
1. MNIST Handwritten digit classification using fully connected ANN model
2. CIFAR-10 image classification with Convolutional Neural Network  (classify images from 10 different category)
   
