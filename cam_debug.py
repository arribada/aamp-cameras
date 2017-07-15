#!/usr/bin/python
# AAMP debug / deployment mode. Streams live feed to phone if connected to access point.

import RPi.GPIO as GPIO
import time
from subprocess import call
from datetime import datetime
import logging

# Logging all of the camera's activity to the "camera_log" file inside the data folder so it is retained between updates.

logging.basicConfig(format='%(asctime)s %(message)s',filename='/data/debug_log',level=logging.DEBUG)
logging.info('AAMP has started in debug mode')

# Automatically go into debug mode and stream camera to a browser to aid with deployment when up in the canopy

print "Entering debug mode for 5 mins"

# mkdir /tmp/stream should be run prior to this script

cmd = raspistill -w 640 -h 480 -q 5 -o /tmp/stream/pic.jpg -tl 100 -t 9999999 -th 0:0:0 &
print 'cmd ' +cmd

# Log that we are now streaming"
logging.info('Streaming has started')
call ([cmd], shell=True)
# call ([perms], shell=True)

stream = LD_LIBRARY_PATH=./ ./mjpg_streamer -i "input_file.so -f /tmp/stream -n pic.jpg" -o "output_http.so -w ./www"
print 'stream ' +stream

# Log that it's possible to connect to the AP"
logging.info('Ready to connect to the AP and visit port 8080')
call ([stream], shell=True)
# call ([perms], shell=True)

# To cancel debug mode you need to remove the jumper cable marked debug. See AAMP instructional video for details.