from gpiozero import LED
from relayUtils import *
from functools import partial

def getLedConfig(MODE='windows'):
	if MODE == 'pi':
		return {	'red': {'pin':LED(16), 'state':'off'},
				 'yellow': {'pin':LED(20), 'state':'off'},
				  'green': {'pin':LED(21), 'state':'off'}}
	elif MODE == 'usb':
		relays = relayBoard()
		relays.loadLib()
		ids = relays.enumDevs()
		if len(ids) > 0:
			relays.openDevById(ids[0])
		else: raise ValueError("No relay board found")

		return {	'driver':relays,
					'red': {'pin':2, 'state':'off'},
				 'yellow': {'pin':3, 'state':'off'},
				  'green': {'pin':4, 'state':'off'},
				 'buzzer': {'pin':1, 'state':'off'}
		}
	elif MODE == 'windows':
		return {	'red': {'pin':16, 'state':'off'},
				 'yellow': {'pin':20, 'state':'off'},
				  'green': {'pin':21, 'state':'off'}}

def setLedState(ledDict, ledName, ledState, MODE='usb', override=False):
	if ledName in ledDict:
		if ledState.casefold() == "ON".casefold():
			if override or ledDict[ledName]['state'] != 'on':
				ledDict[ledName]['state'] = 'on'
				if   MODE == 'pi': 		ledDict[ledName]['pin'].on()
				elif MODE == 'usb': 	ledDict['driver'].closeRelay(ledDict[ledName]['pin'])
				elif MODE == 'windows':	print(ledName + " is now ON")
		elif ledState.casefold() == "OFF".casefold():
			if override or ledDict[ledName]['state'] != 'off':
				ledDict[ledName]['state'] = 'off'
				if   MODE == 'pi': 		ledDict[ledName]['pin'].off()
				elif MODE == 'usb': 	ledDict['driver'].openRelay(ledDict[ledName]['pin'])
				elif MODE == 'windows':	print(ledName + " is now OFF")
		elif ledState.casefold() == "BLINKING".casefold():
			if override or ledDict[ledName]['state'] != 'blinking':
				ledDict[ledName]['state'] = 'blinking'
				if   MODE == 'pi': 		ledDict[ledName]['pin'].blink()
				elif MODE == 'usb': 	ledDict['driver'].blinkRelay(ledDict[ledName]['pin'])
				elif MODE == 'windows':	print(ledName + " is now BLINKING")
		else: raise Exception("LED state must be On or Off")
	else: raise Exception("LED name not valid")

def onFor(ledDict, ledName, MODE='usb', override=False, time=1.0):
        ledDict['driver'].closeRelayFor(ledDict[ledName]['pin'], time)
                                                         

