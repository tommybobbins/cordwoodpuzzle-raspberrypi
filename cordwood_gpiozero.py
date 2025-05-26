#!/usr/bin/python
#Date: 1-May-2014
#Auth: tng@chegwin.org
#Desc: Script to test Cordwood puzzle from boldport.
#      http://boldport.tictail.com/product/cordwood-puzzle
#      http://boldport.com

from gpiozero import LED, LEDBoard
from time import sleep


# Here are the 6 LEDS
leds = LEDBoard(17,27,22,10,9,25)
leds.on()
sleep(0.3)
leds.off()
sleep(0.3)
# Loop through all 6 LEDS
try: 
  while True:
    for led in leds:
      #print ("Switching LED %i" % led)
      led.on()
      sleep(2.0)
      led.off()
      sleep(0.3)
except:
  print(f'Something went wrong')
