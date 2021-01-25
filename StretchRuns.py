# Starting example of reading the Stretch signal on pin 37 and recording the time and rate.
import numpy  as  np
import sys, os, time, datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.IN)

NRuns = int(input("How many runs? "))
NCounts = int(input("How many counts per run? "))
diffarr = []

for i in range(NRuns):
	print("Run", i)
	NCount = 0
	starttime = datetime.datetime.now()
	starttime2 = time.time()
	rundiffarr = []
	while NCount < NCounts:
		if GPIO.input(37)==1:
			timedifference = time.time() - starttime2
			rundiffarr += [timedifference]
			NCount = NCount + 1
			while GPIO.input(37)==1: # Wait for the Stretch signal to fall
				time.sleep(0.00001) 
			starttime2 = time.time()
	endtime = datetime.datetime.now()
	timedifference = endtime - starttime
	nSeconds = timedifference.total_seconds()
	diffarr += [nSeconds]
	
	print("Count rate = ",NCount/nSeconds," Hz")
	print("Average Time Between Counts: ",np.average(rundiffarr),"s")

print("Average Run Time:", np.average(diffarr), "s")
print("Average Count Rate:", NCount/np.average(diffarr), "Hz")
GPIO.cleanup()
