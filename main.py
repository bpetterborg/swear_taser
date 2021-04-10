#!/usr/bin/env python3
#
# tases me everytime I swear
#
# It gets input from Google Cloud Speech Recognition,
# decides if it's a swear from a list, and if it is,
# it sends an arduino the signal to swear me over 
# serial.


# imports
import speech_recognition as sr	# self explanatory 
import serial					# to communicate with arduino

# variables
r = sr.Recognizer()
mic = sr.Microphone(device_index=3) # CHANGE THIS TO THE CORRECT MIC

PORT = '/dev/tty/USB0' # set this to the USB port
arduino = serial.Serial(PORT, 9600, timeout=.1)

# swear list
swears = [
	'fuck',
	'motherfucker', 
	'fucker', 
	'bitch', 
	'bitching', 
	'cum', 
	'shit',
	'shitting',
	'cunt',
	'damn',
	'goddamn',
	'asshole',
	'ass',
	'cock'
]


# connect to arduino over serial, detect swears
while True:
	
	# display messages from arduino
	data = arduino.readline()[:-2]	# [:-2] removes line-endings

	# speech recognition
	with mic as source:

		# adjust for background noise
		r.adjust_for_ambient_noise(source)

		# listen to source
		audio = r.listen(source)

		# run the recognizer on it
		words = r.recognize_google(audio)
		print(words) # print what user says

		if any(element in swears for element in words.split()):
			print('Detected swear, tasing')
			arduino.write(1)

		else:
			print('No swears detected.')
