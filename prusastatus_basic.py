#PrusaStatus.py

import json
import requests
##from gpiozero import LED
from sys import exit
from time import sleep
from datetime import datetime

#TODO: replace with auto-discovery?
printerIP = '192.168.1.2' 
updateTime = 2 #seconds

printerURL = 'http:// ' + printerIP + '/api/printer/job'
leds = {'red': LED(16), 'yellow': LED(20), 'green': LED(21)}

while (1):

	now = datetime.now()

	current_time = now.strftime("%H:%M:%S")
	print("Data Update @", current_time, end = ": ")

	try:
		status = requests.get(printerURL)
	except Exception as e:
		print ("Cannot get data from printer. Failed with error: " + str(e))
	else:
		print ("Raw status: " + status)

		j = json.loads(status.json())
		print ("Job Status JSON: " + str(j))

		state = status['state']

		print ("State: " + str(state))

		if state == "Operational":
			pass
			#Green LED and Yellow LED On
		elif state == "Printing":
			pass
			#Green LED on
		elif state == "Pausing" or state == "Paused" or state == "Cancelling":
			pass
			#Yellow LED on
		elif state == "Error":
			#Red LED Blinking"
			pass
		elif state == "Offline": #TODO: Or Timeout on request
			#Red LED On
			pass
		else: #Some other response we don't know about:
			pass
	finally:
		sleep(2)


