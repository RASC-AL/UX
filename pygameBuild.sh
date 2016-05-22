#!/bin/bash

#
# Build script for pygame 1.9 under Raspbian by Neil Munday (www.mundayweb.com)
# March 2014
#

buildDir=`pwd`/pygame-build
pygameDir=$buildDir/pygame-1.9.1release

echo "Removing system installed pygame..."
sudo apt-get remove python-pygame

echo "Installing dependencies..."
sudo apt-get install libv4l-dev mercurial python-dev python-numpy ffmpeg libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libsdl1.2-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev

if [ ! -e /usr/include/linux/videodev.h ]; then
   if [ ! -e /usr/include/libv4l1-videodev.h ]; then
      echo "Error: /usr/include/libv4l1-videodev.h does not exist!"
      exit 1
   fi
   sudo ln -s /usr/include/libv4l1-videodev.h /usr/include/linux/videodev.h
fi

mkdir -p $buildDir

cd $buildDir

if [ -e $pygameDir]; then
   echo "Removing previous pygame source"
   rm -rf $pygameDir
fi

echo "Downloading pygame source..."
wget http://www.pygame.org/ftp/pygame-1.9.1release.tar.gz

echo "Unpacking pygame source..."
tar xvfz pygame-1.9.1release.tar.gz
echo "Patching joystick.c ..."
cd pygame-1.9.1release
cp src/joystick.c src/joystick.c-orig
grep -v printf src/joystick.c-orig > src/joystick.c

echo "Building pygame (this will take some time!) ..."
python setup.py build

echo "Installing pygame..."
sudo python setup.py install

echo "Done!"
