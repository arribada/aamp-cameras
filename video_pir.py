#!/usr/bin/python
# AAMP video triggered by PIR, default 5 seconds per video 

import RPi.GPIO as GPIO
import time
from subprocess import call
from datetime import datetime
import logging

# Logging all of the camera's activity to the "camera_log" file inside the data folder so it is retained between updates.

logging.basicConfig(format='%(asctime)s %(message)s',filename='/data/camera_log',level=logging.DEBUG)
logging.info('AAMP camera started up successfully')

# Assigning a variable to the pins that we have connected the PIR to
sensorPin = 4

# Setting the GPIO (General Purpose Input Output) pins up so we can detect if they are HIGH or LOW (on or off)

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Defining our default states so we can detect a change

prevState = False
currState = False

# Starting a loop

while True:
    time.sleep(0.1)
    prevState = currState

    # Map the state of the camera to our input pins (jumper cables connected to your PIR)
    currState = GPIO.input(sensorPin)

    # Checking that our state has changed   
    if currState != prevState:
    # About to check if our new state is HIGH or LOW

        newState = "HIGH" if currState else "LOW"
   
        print "GPIO pin %s is %s" % (sensorPin, newState)

        if currState:  # Our state has changed, so that must be a trigger from the PIR       
     
            i = datetime.now() # Get the time now
            get_date = i.strftime('%Y-%m-%d') # Get and format the date
            get_time = i.strftime('%H-%M-%S.%f') # Get and format the time

            # Recording that a PIR trigger was detected
            logging.info('PIR trigger detected')

            # Assigning a variable so we can create a video .h264 file that contains the date and time as its name
            video = get_date + '_' +  get_time + '.h264'

            # Using the raspivid library to take a 5 second video
            cmd = 'raspivid -t 5000 -w 800 -h 600 -o /data/' + video 
			print 'cmd ' +cmd          

            # Log that we have just taken a video
            logging.info('About to take a video and save to the /data folder')
            call ([cmd], shell=True)
            # call ([perms], shell=True)
            
            # Log that a photo was taken successfully and state the file name so we know which one"
            logging.info('Video taken successfully %(show_video_name)s', { 'show_video_name': video })
            photo_location =  '/data/' + video                   

        else:

           # print "Waiting for a new PIR trigger to continue"
           logging.info('Waiting for a new PIR trigger to continue')

# END