#!/usr/bin/python
# AAMP photo timelapse

import os, sys
import datetime
from os import system
from time import sleep
from picamera import PiCamera
import picamera

import os, sys

get_date = datetime.datetime.now().strftime("%Y-%m-%d")

# Path to be created
path = "/data/%s" % get_date

try:
    os.mkdir( path, 0755 );
except OSError:
    pass

print "Create new directory {timestamp:%Y-%m-%d}"

camera = picamera.PiCamera()
picamera.PiCamera.CAPTURE_TIMEOUT = 60

camera.resolution = (1080, 720)

sleep(2)
for filename in camera.capture_continuous('/data/{timestamp:%Y-%m-%d}/img{counter:03d}_{timestamp:%Y-%m-%d-%H-%M}.jpg'):
    print('Captured %s' % filename)
    sleep(120) # wait 2 mins