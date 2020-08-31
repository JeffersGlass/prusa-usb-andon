#PrusaStatus.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import logging
from gpiozero import LED
from time import sleep
from datetime import datetime
from prusaStatusHardware import *

logging.basicConfig(level=logging.WARNING)

#TODO: replace with auto-discovery?
printerIP = '192.168.1.2' 
updateTime = 2 #seconds

#exclude switches to remove "Being Controlled by Automated Software" banner
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("disable-extensions-file-access-checks")
#chrome_options.add_experimental_option("excludeSwitches",['enable-automation'])
chrome_options.add_argument("start-fullscreen")
chrome_options.add_argument("disable-infobars")
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://" + printerIP)

leds = getLedConfig()

try:
	driver.get("http://192.168.1.2")
	quitButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'delete')))
except Exception as e:
	logging.warning ("Cannot open Selenium. Failed with error: " + str(e))
else:

	quitButton.click()
	logging.info("Quit Button Clicked")
	'''#1530, 102
	#1891, 25
	#temp = driver.find_element_by_link_text('Temperatures')
	#ac = ActionChains(driver)
	#for x in range(250, 150, -10):
		for y in range(-70, -50, 5):
			print(str(x) + "," + str(y))
			ac.move_to_element(temp).move_by_offset(x,y).click().perform()
			
			#logging.warning("Clicked x:" + str(x) + " y:" + str(y))
			#sleep(.1)'''
	while (1):

		now = datetime.now()
 
		current_time = now.strftime("%H:%M:%S")
		logging.info("Data Update @" + current_time)

		elem = driver.find_element_by_class_name("prusa-line")
		t = elem.text
		logging.debug("ELEMENT TEXT:" + str(t))


		ind = "Printer status:"
		statusStart = t.index(ind) + len(ind)
		state = t[statusStart:].split("\n")[0].strip(" ")
		logging.debug("StateText:<" + str(state) + ">")

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

		sleep(updateTime)


