#!/usr/bin/env python3
#
# tases me everytime I swear
#
# It gets input from Google Cloud Speech Recognition,
# checks if it's a swear from a list, and if it is,
# it sends an arduino the signal to tase me over 
# serial.

# imports
import speech_recognition as sr	# self explanatory 
import serial					# to communicate with arduino

# variables
r = sr.Recognizer()
mic = sr.Microphone() # CHANGE THIS TO THE CORRECT MIC (FIXME)

PORT = '/dev/ttyUSB0' # set this to the USB port
arduino = serial.Serial(PORT, 9600, timeout=.1)

swears = open('swears.txt','r').read().split()



# connect to arduino over serial, detect swears
#while True:
#	
#	# display messages from arduino
	# data = arduino.readline()[:-2]	# [:-2] removes line-endings

	# # speech recognition
	# with mic as source:

	# 	# adjust for background noise
	# 	r.adjust_for_ambient_noise(source)
# 
#		# listen to source
#		audio = r.listen(source)
#		# run the recognizer on it
#		words = r.recognize_google(audio)
#		print(words) # print what user says
#
#		if any(element in swears for element in words.split()):
#			print('Detected swear, tasing')
#			arduino.write(1)
#
#		else:
#			print('No swears detected.')



try:
	# adjust for background noise
	with mic as source: 
		r.adjust_for_ambient_noise(source)
	
	while True:

		print('Ready')
		
		# getting serial data from arduino
		data = arduino.readline()[:-2]	# [:-2] removes line-endings
		print('data')

		with mic as source: 
			audio = r.listen(source)
		
		print('Recognizing...')
		
		try:
			# recognize speech
			value = r.recognize_google(audio)

			# print it as unicode TODO: Remove this
			#if str is bytes:  # this one for python2
			#	print(u"You said {}".format(value).encode("utf-8"))
			
			# this one is for python3
			#else:
			print("{}".format(value))

			print(value)

			# determine if any of the words are swears TODO: Add thing to read swears from file
			if any(element in swears for element in value.split()): # may need to do extra processing
				print('Detected Keyword. Tasing.')
				arduino.write(1) # send a 1 to arduino

		
		except sr.UnknownValueError:
			print('Unrecognized. Try again.')
		
		except sr.RequestError as error:
			print("Unable to get results from Google Cloud Speech Recognition Library; {0}".format(error))

# ctrl+c to exit
except KeyboardInterrupt:
	pass