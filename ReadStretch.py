# Starting example of reading the Stretch signal on pin 37 and recording the time and rate.
import numpy  as  np
import sys, os, time, datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.IN)

# Loop while checking for a high signal on pin 37
NCount = 0
starttime = datetime.datetime.now()
starttime2 =  time.time()
try:
    while NCount < 100:
        if GPIO.input(37)==1:
            print(NCount)
            timedifference = time.time() - starttime2
            print(datetime.datetime.now())
            NCount = NCount + 1
            while GPIO.input(37)==1: # Wait for the Stretch signal to fall
                time.sleep(0.00001) 

finally:
    endtime = datetime.datetime.now()
    timedifference = endtime - starttime
    nSeconds = timedifference.total_seconds()
    print("")
    print("Total count = ",NCount)
    print("Count rate = ",NCount/nSeconds," Hz")
    GPIO.cleanup()
