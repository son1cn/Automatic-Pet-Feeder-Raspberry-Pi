#SpinBin
#https://stackoverflow.com/questions/45488233/controlling-continuous-servo-using-python-in-raspberry-pi-but-the-continuous-ser
#imports
import RPi.GPIO as GPIO
from gpiozero import LightSensor
import pigpio
import time
import signal
import atexit

led_pin = 5
servoPIN = 13
CW = 1565
STOP = 1500
pi = pigpio.pi()
#setting up LightSensor on pin 4
ldr = LightSensor(4)



try:
    while True:
        print("LED turn on")
        pi.write(led_pin, 1)
        time.sleep(1)
        print(ldr.value)
        if ldr.value > 0.8:
            print("moving away from light")
            while ldr.value > 0.7:
                pi.set_servo_pulsewidth(servoPIN, CW)
                time.sleep(0.1)
                pi.set_servo_pulsewidth(servoPIN, STOP)
                time.sleep(0.5)
            print("final escape ldr ",ldr.value)
        print("starting servo")
        print("starting ldr ", ldr.value)
        while ldr.value < 0.8:
            print("current LDR: " + str(ldr.value))
            pi.set_servo_pulsewidth(servoPIN, CW)
            time.sleep(0.1)
            pi.set_servo_pulsewidth(servoPIN, STOP)
            time.sleep(0.2)
        print("final ldr ",ldr.value)
        print("Motor stopped, LED Off")
        pi.write(led_pin, 0)
        time.sleep(5)
except KeyboardInterrupt:
    pi.stop()
