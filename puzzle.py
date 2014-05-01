#!/usr/bin/python
#Date: 1-May-2014
#Auth: tng@chegwin.org
#Desc: Script to test Cordwood puzzle from boldport.
#      http://boldport.tictail.com/product/cordwood-puzzle
#      http://boldport.com

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
# We are using Pins 11,13,15,19,21 and 22 to connect to the control end
# and pin 1 and 5 to connect to 3.3V and GND respectively.

# Here are the 6 LEDS
leds = [17,27,22,10,9,25]

# Initialize
for led in leds:
    GPIO.setup(led, GPIO.OUT, initial=0) # sets led to output and 0V, off 

# Loop through all 6 LEDS
try: 
    while True:
        for led in leds:
            print ("Switching LED %i" % led)
            GPIO.output(led, 1) # sets port on
            sleep(0.3)
            GPIO.output(led, 0) # sets port off
finally:
    GPIO.cleanup()
