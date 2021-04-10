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
import time						#
import csv						# for reading swear list 

# variables
r = sr.Recognizer()
mic = sr.Microphone(device_index=3) # CHANGE THIS TO THE CORRECT MIC

PORT = '/dev/tty/USB0' # set this to the USB port
arduino = serial.Serial(PORT, 9600, timeout=.1)


# connect to arduino over serial, detect swears
while True:
	
	# display messages from arduino
	data = arduino.readline()[:-2]	# thing on end removes line-endings

	# speech recognition
	with mic as source:

		# adjust for background noise
		r.adjust_for_ambient_noise(source)

		# listen to source
		audio = r.listen(source)

		# run the recognizer on it
		r.recognize_google(audio)

		with open('swears.csv', 'rt') as f:
			reader = csv.reader(f, delimiter=',')

			for row in reader:
				if words == row[0]:
					print("is in file")

