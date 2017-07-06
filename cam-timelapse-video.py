#!/usr/bin/python
# AAMP video timelapse

import picamera
from os import system
import time

# Set the resolution of the video you intend to capture.
camera = picamera.PiCamera(resolution=(1920, 1080))

print "Starting up!"
time.sleep(60)
print "Waiting 60 seconds"
# Change the time.sleep value to delay the startup. The variable is in seconds, so it waits 60 seconds before starting by default

x = 1
y = 1
while True:
     print "Taking a video. This is video %d " % (x)
     camera.start_recording('%d.h264' % y)
     camera.wait_recording(5)
	 # Record for 5 seconds
     camera.stop_recording()
     print "Sleeping for 10 mins before recording again"
     time.sleep(600)
	 # Waiting for 10 mins before continuing
     y += 1
     print "Done. Preparing to record next video."
x += 1