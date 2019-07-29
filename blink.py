#info pulled from https://iotguider.in/raspberrypi/blinking-led-with-raspberry-pi/

import RPi.GPIO as GPIO
import time
#using GPIO pin/channel 5 for blink test
GPIO.setmode(GPIO.BCM)
GPIO.setup(5,GPIO.OUT)
while True:
	GPIO.output(5, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(5, GPIO.LOW)
	time.sleep(1)
