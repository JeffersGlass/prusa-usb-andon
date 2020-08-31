#PrusaStatus.py

import json
import requests
import logging
from gpiozero import LED
from time import sleep
from datetime import datetime
from prusaStatusHardware import *

logging.basicConfig(level=logging.WARNING)
MODE = "windows"
#MODE = "pi"

#TODO: replace with auto-discovery?
printerIP = '192.168.1.2' 
updateTime = 1 #seconds

printerURL = 'http:// ' + printerIP + '/api/printer/job'
leds = getLedConfig(MODE)

while (1):

	now = datetime.now()

	current_time = now.strftime("%H:%M:%S")
	logging.info("Data Update @" + current_time)

	try:
		if MODE == 'pi': status = requests.get(printerURL)
		else: status = json.dumps({"job": "myPrintFile.gcode", "progress": "75", "state": "Error"})
	except Exception as e:
		logging.warning ("Cannot get data from printer. Failed with error: " + str(e))
	else:
		logging.info ("Raw status: " + status)

		j = json.loads(status)
		logging.info ("Job Status JSON: " + str(j))

		state = j['state']

		logging.info ("State: " + str(state))

		if state == "Operational":
			setLedState(leds, 'green', 'on')
			setLedState(leds, 'yellow', 'on')
			setLedState(leds, 'red', 'off')
			#Green LED and Yellow LED On
		elif state == "Printing":
			setLedState(leds, 'green', 'on')
			setLedState(leds, 'yellow', 'off')
			setLedState(leds, 'red', 'off')
			#Green LED on
		elif state == "Pausing" or state == "Paused" or state == "Cancelling":
			setLedState(leds, 'green', 'off')
			setLedState(leds, 'yellow', 'on')
			setLedState(leds, 'red', 'off')
			#Yellow LED on
		elif state == "Error":
			setLedState(leds, 'green', 'off')
			setLedState(leds, 'yellow', 'off')
			setLedState(leds, 'red', 'blinking')
			#Red LED Blinking"
		elif state == "Offline": #TODO: Or Timeout on request
			setLedState(leds, 'green', 'off')
			setLedState(leds, 'yellow', 'off')
			setLedState(leds, 'red', 'on')
		else: #Some other response we don't know about:
			setLedState(leds, 'green', 'blinking')
			setLedState(leds, 'yellow', 'blinking')
			setLedState(leds, 'red', 'blinking')
	finally:
		sleep(updateTime)


