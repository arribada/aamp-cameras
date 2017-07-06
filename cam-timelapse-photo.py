#!/usr/bin/python
# AAMP photo timelapse

from picamera import PiCamera
from os import system
from time import sleep

camera = PiCamera()
camera.resolution = (1920, 1080)

for i in range(720):
    camera.capture('image{0:04d}.jpg'.format(i))
    sleep(120)