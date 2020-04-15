#SpinBin
#https://stackoverflow.com/questions/45488233/controlling-continuous-servo-using-python-in-raspberry-pi-but-the-continuous-ser
#imports
import RPi.GPIO as GPIO
from gpiozero import LightSensor
from gpiozero import Servo
import time
import signal
import atexit

atexit.register(GPIO.cleanup)

#pin init
led_pin = 5

#servoPIN = 26

GPIO.setmode(GPIO.BCM)
#GPIO.setup(servoPIN, GPIO.OUT, initial=False)
#GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT, initial=False)
servo = Servo(26)

#p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
#p.start(0) # Initialization

#setting up LightSensor on pin 4
ldr = LightSensor(4)
#while True:
    #just print value to help figure out setup rc value for algorithm
#   print(ldr.value)

time.sleep(2)

try:
    while True:
        print("LED turn on")
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(1)
        print(ldr.value)
        #need to get away from light
        if ldr.value > 0.8:
            print("moving away from light")
            servo.value = 0.5
 #           p.start(0)
 #           p.ChangeDutyCycle(7.2)
            while ldr.value > 0.7:
                time.sleep(0.05)
                #print(ldr.value)
            print("final escape ldr ",ldr.value)
#            p.stop()
            servo.value = 0
        print("starting servo")
        print("starting ldr ", ldr.value)
#        p.start(0)
#        p.ChangeDutyCycle(6.9)
        servo.value = 0.5
        while ldr.value < 0.8:
            #print(ldr.value)
            time.sleep(0.05)
        print("final ldr ",ldr.value)
#        p.stop()
        servo.value = 0
        print("Motor stopped, LED Off")
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(5)
except KeyboardInterrupt:
#  p.stop()
  servo.value = 0
  GPIO.cleanup()
