#!/usr/bin/python


import time
import virtGPIO as GPIO

myServo = GPIO.Servo(7)   # servo on pin 7
c=0

while True:
    print(c)
    c += 5

    if (c>127):  # limit to 127
        c=0

    myServo.write(c)   # sweeps slowly 0 - 127 degrees then returns

    time.sleep(2)

    myServo.stop()    # detaches (You DONT have to do it this way)

    time.sleep(0.2)
