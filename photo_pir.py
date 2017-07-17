#!/usr/bin/python
# AAMP photo triggered by PIR

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
    # prevBattState = currBattState
    
    # Map the state of the camera to our input pins (jumper cables connected to your PIR)

    currState = GPIO.input(sensorPin)
    # currBattState = GPIO.input(lowbattPin)

    # Checking that our state has changed
   
    if currState != prevState:
    # About to check if our new state is HIGH or LOW

        newState = "HIGH" if currState else "LOW"
        #  newBattState = "HIGH" if currBattState else "LOW"        
        print "GPIO pin %s is %s" % (sensorPin, newState)

        if currState:  # Our state has changed, so that must be a trigger from the PIR       
     
            i = datetime.now() # Get the time now
            get_date = i.strftime('%Y-%m-%d') # Get and format the date
            get_time = i.strftime('%H-%M-%S.%f') # Get and format the time
            # Checking the current status of the battery

            logging.info('PIR trigger detected')

            # Assigning a variable so we can create a photo JPG file that contains the date and time as its name
            photo = get_date + '_' +  get_time + '.jpg'

            # Using the raspistill library to take a photo. You can show that a photo has been taken in a small preview box on the desktop by changing --nopreview to --preview
            cmd = 'raspistill -t 300 -w 1920 -h 1440 --nopreview -o /data/' + photo 
	    print 'cmd ' +cmd

            # If you find you have permission problems saving to other attached non-Naturebytes storage devices you can use this line to change the owner of the photo if required
            # perms = 'chown pi:pi /media/usb0/' + photo
            # print 'perms ' +perms            

            # Log that we have just taking a photo"
            logging.info('About to take a photo and save to /data')
            call ([cmd], shell=True)
            # call ([perms], shell=True)
            
            # Log that a photo was taken successfully and state the file name so we know which one"
            logging.info('Photo taken successfully %(show_photo_name)s', { 'show_photo_name': photo })
            photo_location =  '/data/' + photo                        

        else:

           # print "Waiting for a new PIR trigger to continue"
           logging.info('Waiting for a new PIR trigger to continue')

# END