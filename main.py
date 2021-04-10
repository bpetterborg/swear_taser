#!/usr/bin/env python3

# tasers me when i swear


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

# open swears list
swears_file = open('swears.csv')

with open(swears_file, newline='') as csvfile:
	swears_list = list(csv.reader(csvfile))


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

		if input in swears_list:
			arduino.write('1')

