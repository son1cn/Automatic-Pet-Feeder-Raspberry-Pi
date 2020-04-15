import RPi.GPIO as GPIO
import time

servoPIN = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(0) # Initialization
time.sleep(2)
try:
  while True:
    p.ChangeDutyCycle(6.9)
    print("6.9")
    time.sleep(2)
    p.ChangeDutyCycle(6.8)
    print("6.8")
    time.sleep(2)
#    p.ChangeDutyCycle(3.5)
#    time.sleep(5)
#    p.ChangeDutyCycle(12.5)
#    time.sleep(5)
#    p.ChangeDutyCycle(10)
#    time.sleep(5)
#    p.ChangeDutyCycle(7.5)
#    time.sleep(5)
#    p.ChangeDutyCycle(5)
#    time.sleep(5)
#    p.ChangeDutyCycle(2.5)
#    time.sleep(5)
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
