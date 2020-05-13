#This file turns off LED on Pin 5

import RPi.GPIO as GPIO
import time
#using GPIO pin/channel 5 for blink test
GPIO.setmode(GPIO.BCM)
GPIO.setup(5,GPIO.OUT)
GPIO.output(5, GPIO.LOW)
GPIO.cleanup(5)

