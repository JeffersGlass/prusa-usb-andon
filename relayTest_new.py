#relayTest.py

import sys, os, time
import ctypes
import logging

from relayUtils import *

def ctest():
	relays = relayBoard()
	relays.loadLib()
	ids = relays.enumDevs()
	if len(ids) > 0:
		relays.openDevById(ids[0])
	else: exit("No relay board found")
	
	relays.closeRelay(1)
	time.sleep(1)
	relays.openRelay(1)
	time.sleep(1)

	relays.closeAllRelays()
	time.sleep(1)
	relays.openAllRelays()
	time.sleep(1)
	
	relays.blinkRelay(1)
	time.sleep(10)

	relays.blinkRelay(2)
	time.sleep(10)

	relays.blinkRelay(3)
	time.sleep(10)
	
	relays.noBlink(1)
	time.sleep(5)	
	relays.openAllRelays()
	relays.closeDev()
	relays.unloadLib()
	
 

def main():
	logging.basicConfig(level=logging.DEBUG)

	print("Starting test")
	ctest()
	print("Ending test")


'''def main():
	print("Test 4-ch relay")
	loadLib()
	getLibFunctions()
	try:
		print("Searching for compatible devices")
		global devids
		devids = enumDevs()
		if len(devids) != 0 :
			# Test any 1st found dev .
			print("Testing relay with ID=" + devids[0])
			openDevById(devids[0])
			ctest()
			closeDev()
	finally:  
		unloadLib()'''

if __name__ == "__main__" :
  main()