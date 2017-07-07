#!/usr/bin/python
# AAMP photo timelapse

from os import system
from time import sleep
from picamera import PiCamera

file_path = "/data/{timestamp:%Y-%m-%d}"
directory = os.path.dirname(file_path)

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

camera = PiCamera()
camera.resolution = (1920, 1080)

sleep(2)
for filename in camera.capture_continuous('/data/{timestamp:%Y-%m-%d}/img{counter:03d}_{timestamp:%Y-%m-%d-%H-%M}.jpg'):
    print('Captured %s' % filename)
    sleep(120) # wait 2 mins