#This file uses different pulsewidths to find the value that corresponds to barely moving on a continuous servo on pin 13


import pigpio
import time  
import signal  

servo = pigpio.pi()
servo.set_servo_pulsewidth(13, 1500)
time.sleep(5)  

#steps = [800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700]
#steps = [1400, 1410, 1415, 1420, 1425]
#steps = [1420, 1425, 1430, 1435, 1440]
steps = [1555, 1560, 1565, 1500]

#1565 is just moving in clockwise direction

for step in steps:
    print("step " + str(step))
    servo.set_servo_pulsewidth(13, step)
    time.sleep(5)
