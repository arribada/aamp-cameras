#!/usr/bin/python
# AAMP photo timelapse

from os import system
from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1920, 1080)

sleep(2)
for filename in camera.capture_continuous('/data/{timestamp:%Y-%m-%d}/img{counter:03d}_{timestamp:%Y-%m-%d-%H-%M}.jpg'):
    print('Captured %s' % filename)
    sleep(120) # wait 2 mins