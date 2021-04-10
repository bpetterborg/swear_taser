#!/usr/bin/env python3

# tasers me when i swear


# imports
import speech_recognition as sr   # self explanetory 
import serial                     # to communicate with arduino
import time

# variables
r = sr.Recognizer()
mic = sr.Microphone(device_index=3) # CHANGE THIS TO THE CORRECT MIC

PORT = '/dev/tty/USB0' # set this to the USB port
arduino = serial.Serial(PORT, 9600, timeout=.1)

with mic as source:

	# adjust for background noise
	r.adjust_for_ambient_noise(source)

	# listen to source
	audio = r.listen(source)

	# run the recognizer on it
	r.recognize_google(audio)