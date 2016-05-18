#!/bin/bash
# Script to install opencv3: http://www.pyimagesearch.com/2015/07/20/install-opencv-3-0-and-python-3-4-on-ubuntu/
apt-get update
apt-get upgrade

# Get the essential tools and things for video and image processing - need to
# test a minimal install
apt-get install build-essential cmake git pkg-config
apt-get install libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev
apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
apt-get install libgtk2.0-dev
apt-get install libatlas-base-dev gfortran

# Setup python
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py
# Install virtualenv if it's not there
pip3 install virtualenv virtualenvwrapper
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh

source ~/.bashrc

#mkvirtualenv cv
apt-get install python3.4-dev
pip install numpy

# Install openCV3
cd ~
git clone https://github.com/Itseez/opencv.git
cd opencv
git checkout 3.1.0

cd ~
git clone https://github.com/Itseez/opencv_contrib.git
cd opencv_contrib
git checkout 3.1.0

cd ~/opencv
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_INSTALL_PREFIX=/usr/local \
	-D INSTALL_C_EXAMPLES=ON \
	-D INSTALL_PYTHON_EXAMPLES=ON \
	-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
	-D BUILD_EXAMPLES=ON ..

make -j4

make install
ldconfig

# Link openCV
cd ~/.virtualenvs/cv/lib/python3.4/site-packages/
ln -s /usr/local/lib/python3.4/site-packages/cv2.cpython-34m.so cv2.so
