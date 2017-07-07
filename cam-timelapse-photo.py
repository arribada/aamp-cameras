#!/usr/bin/python
# AAMP photo timelapse

import os, sys
import datetime
from os import system
from time import sleep
from picamera import PiCamera

import os, sys

get_date = datetime.datetime.now().strftime("%Y-%m-%d")

# Path to be created
path = "/data/%s" % get_date

try:
    os.mkdir( path, 0755 );
except OSError:
    pass

print "Create new directory {timestamp:%Y-%m-%d}"

camera = PiCamera()
camera.resolution = (1920, 1080)

sleep(2)
for filename in camera.capture_continuous('/data/{timestamp:%Y-%m-%d}/img{counter:03d}_{timestamp:%Y-%m-%d-%H-%M}.jpg'):
    print('Captured %s' % filename)
    sleep(120) # wait 2 mins