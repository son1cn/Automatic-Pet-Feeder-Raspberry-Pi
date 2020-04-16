import RPi.GPIO as GPIO  
import pigpio
import time  
import signal  
import atexit  

#atexit.register(GPIO.cleanup)    

#GPIO.setmode(GPIO.BCM)  
#GPIO.setup(13, GPIO.OUT, initial=False)  
#p = GPIO.PWM(13,50) #50HZ  
#p.start(0)
servo = pigpio.pi()
time.sleep(2)  

STEPS=10    # the number of steps either side of nominal
NOMINAL=7.5 # the 'zero' PWM %age
RANGE=1   # the maximum variation %age above/below NOMINAL

while(True):  
    # loop first over "forward" ramp up/down, then reverse.
    for direction in [+1.0,-1.0]:
        # step from 0 to 100% then back to just above zero
        # (next time round the loop will do the 0)
        for step in list(range(STEPS+1))+list(range(STEPS-1,0,-1)):
            dutycycle = NOMINAL + direction*RANGE*step/STEPS
            print (direction, step, dutycycle)
            servo.set_servo_pulsewidth(13, 1500)
            #p.ChangeDutyCycle(dutycycle)  
            time.sleep(1.0) 