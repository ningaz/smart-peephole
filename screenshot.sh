#!/bin/sh

/home/root/bin/ffmpeg/ffmpeg -s 320x240 -f video4linux2 -y -i /dev/video0 -vframes 1 image.jpeg
