# tflite_micro_rpi0
Running Tensorflow Lite runtime in Python on Raspberry Pi Zero and Zero W running Bullseye Python V 3.9  <br>
**Install Prequisite packages** <br>
1. Installing OpenCV on Raspberry Pi Zero/Zero W <br>
Install Required libraries required by OpenCV
```
sudo apt install libxrender1 libx265-192 libxi6 ocl-icd-libopencl1 libxcb-render0 libtwolame0 libwebpmux3 libvorbisenc2 libsrt1.4-gnutls libgraphite2-3 libva-x11-2 libwayland-egl1 libgme0 libmp3lame0 libcairo-gobject2 libspeex1 libavcodec58 libswresample3 libdav1d4 libdrm2 libxvidcore4 libtheora0 libxfixes3 libvpx6 libvdpau1 libwayland-client0 libharfbuzz0b libatlas3-base libzmq5 libudfread0 libssh-gcrypt-4 libmpg123-0 libaom0 libgdk-pixbuf-2.0-0 libogg0 libpangocairo-1.0-0 libxcb-shm0 libbluray2 librabbitmq4 libpgm-5.3-0 libopenmpt0 libpangoft2-1.0-0 libatspi2.0-0 libwayland-cursor0 libcodec2-0.9 libxrandr2 libxinerama1 libxcomposite1 libgtk-3-0 libxkbcommon0 libva-drm2 libgsm1 librsvg2-2 libopenjp2-7 libxdamage1 libpixman-1-0 libswscale5 libavutil56 libsodium23 libcairo2 libatk1.0-0 libpango-1.0-0 libthai0 libxcursor1 libavformat58 libopus0 libdatrie1 libvorbis0a libsoxr0 libva2 libatk-bridge2.0-0 libzvbi0 libshine3 libx264-160 libvorbisfile3 libepoxy0 libchromaprint1 libwavpack1 libgfortran5 libnorm1 libsnappy1v5
```

Then install OpenCV using pip:
```
  pip3 install opencv-python==4.6.0.66
```
2. Installing TF-LITE-MICRO runtime packages <br>

   
   
