#SpinBin
#https://stackoverflow.com/questions/45488233/controlling-continuous-servo-using-python-in-raspberry-pi-but-the-continuous-ser
#imports
from gpiozero import LightSensor
import pigpio
import time, csv
from datetime import datetime

#LED is connected to pin 5
led_pin = 5
#Continuous servo is on pin 13 (one of the hardware PWM channels)
servoPIN = 13
#microseconds of pulsewidth corresponding to slowest Clockwise movement of my particular servo
CW = 1565
#microseconds of stopped servo
STOP = 1500
#init of pigpio
pi = pigpio.pi()
#setting up LightSensor on pin 4
#All LDR values further down need to be calibrated for your setup
ldr = LightSensor(4)

def write_log():
    try:
        with open('feeder_log.csv', 'w') as outfile:
            outwrite = csv.writer(outfile)
	    message = [datetime.now().strftime("%d/%m/%Y %H:%M:%S")]
            outwrite.writerow(message)
    except Exception as e:
        print(e)
    return

def write_debug_log(output):
    try:
        with open('feeder_debug_log.csv', 'a') as outfile:
            outwrite = csv.writer(outfile)
	    message = [datetime.now().strftime("%d/%m/%Y %H:%M:%S"),output]
            outwrite.writerow(message) 
            print(output)
    except Exception as e:
        print(e)
    return

try:
    while True:
        write_debug_log("LED turn on")
        #print("LED turn on")
        pi.write(led_pin, 1)
        print(ldr.value)
	    #if something is wrong with LDR it returns 0.0
        if ldr.value == 0.0:
            write_debug_log("you shouldn't see this")
            ldr.close()
            time.sleep(1)
            ldr = LightSensor(4)
        #If LDR has higher than 0.8 (for my setup) move a bit before collecting LDR input
        if ldr.value > 0.8:
            write_debug_log("moving away from light")
            #variable to catch LDR problems
            catch = 0
            #moves away from light in 0.1s increments of slowest servo movement
            while ldr.value > 0.8:
            #catch problems with not seeing a reduction in LDR value within 5 steps
                if catch > 4:
                    write_debug_log("LDR not reducing")
                    break
                else:
                    catch += 1
                    pi.set_servo_pulsewidth(servoPIN, CW)
                    time.sleep(0.1)
                    pi.set_servo_pulsewidth(servoPIN, STOP)
                    time.sleep(0.5)
        write_debug_log(ldr.value)
        write_debug_log("final escape ldr " + str(ldr.value))
        write_debug_log("starting servo")
        write_debug_log("starting ldr " + str(ldr.value))
        #while LDR is <0.8 continue to move in 0.1s increments of slowest servo speed
        while ldr.value < 0.8:
            write_debug_log("current LDR: " + str(ldr.value))
            pi.set_servo_pulsewidth(servoPIN, CW)
            time.sleep(0.1)
            pi.set_servo_pulsewidth(servoPIN, STOP)
            time.sleep(0.2)
        write_debug_log("final ldr " + str(ldr.value))
        #turn off LED
        write_debug_log("Motor stopped, LED Off")
        pi.write(led_pin, 0)
        write_log()
        break
except KeyboardInterrupt:
    pi.stop()
