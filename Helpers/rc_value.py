#info pulled from https://iotguider.in/raspberrypi/interfacing-light-dependent-resistor-ldr-in-raspberry-pi/

from gpiozero import LightSensor
import time
#setting up LightSensor on pin 4
ldr = LightSensor(4)
while True:
	#just print value to help figure out setup rc value for algorithm
	print(ldr.value)
	#print every 0.1 secs
	time.sleep(0.1)
