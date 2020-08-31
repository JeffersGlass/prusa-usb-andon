from gpiozero import LED

def getLedConfig(MODE='windows'):
	if MODE == 'pi':
		return {	'red': {'pin':LED(16), 'state':'off'},
				 'yellow': {'pin':LED(20), 'state':'off'},
				  'green': {'pin':LED(21), 'state':'off'}}
	elif MODE == 'windows':
		return {	'red': {'pin':16, 'state':'off'},
				 'yellow': {'pin':20, 'state':'off'},
				  'green': {'pin':21, 'state':'off'}}

def setLedState(ledDict, ledName, ledState, MODE='windows'):
	if ledName in ledDict:
		if ledState.casefold() == "ON".casefold():
			if ledDict[ledName]['state'] != 'on':
				ledDict[ledName]['state'] = 'on'
				ledDict[ledName]['pin'].on() if MODE=='pi' else print(ledName + " is now ON")
		elif ledState.casefold() == "OFF".casefold():
			if ledDict[ledName]['state'] != 'off':
				ledDict[ledName]['state'] = 'off'
				ledDict[ledName]['pin'].off() if MODE=='pi' else print(ledName + " is now OFF")
		elif ledState.casefold() == "BLINKING".casefold():
			if ledDict[ledName]['state'] != 'blinking':
				ledDict[ledName]['state'] = 'blinking'
				ledDict[ledName]['pin'].blink() if MODE=='pi' else print(ledName + " is now BLINKING")
		else: raise Exception("LED state must be On or Off")
	else: raise Exception("LED name not valid")

