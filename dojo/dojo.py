#!/usr/bin/env python

"""
Primeira versao do Dojo com pcDuino programada por Luciano Ramalho na 
Noite do Mini PC em 29/mai/2013 no Garoa Hacker Clube
"""

# fonte:
# https://learn.sparkfun.com/tutorials/programming-the-pcduino/accessing-gpio-pins	
# https://learn.sparkfun.com/tutorials/programming-the-pcduino/analog-input-and-output

import time, os

## For simplicity's sake, we'll create a string for our paths.
GPIO_MODE_PATH= os.path.normpath('/sys/devices/virtual/misc/gpio/mode/')
GPIO_PIN_PATH=os.path.normpath('/sys/devices/virtual/misc/gpio/pin/')
GPIO_FILENAME="gpio"
ADC_PATH= os.path.normpath('/proc/')
ADC_FILENAME = "adc"

## create empty arrays to store the pointers for our files
pinMode = []
pinData = []
adcFiles = []

## Create a few strings for file I/O equivalence
HIGH = "1"
LOW =  "0"
INPUT = "0"
OUTPUT = "1"
INPUT_PU = "8"

def setup():

	## First, populate the arrays with file objects that we can use later.
	for i in range(18):
		pinMode.append(os.path.join(GPIO_MODE_PATH, 'gpio'+str(i)))
		pinData.append(os.path.join(GPIO_PIN_PATH, 'gpio'+str(i)))

	for i in range(6):
		adcFiles.append(os.path.join(ADC_PATH, ADC_FILENAME+str(i)))

	## Now, let's make all the pins outputs...
	for pin in pinMode:
		file = open(pin, 'r+')  ## open the file in r/w mode
		file.write(OUTPUT)      ## set the mode of the pin
		file.close()            ## IMPORTANT- must close file to make changes!

	## ...and make them low.
	for pin in pinData:
		file = open(pin, 'r+')
		file.write(LOW)
		file.close()

def set(pin, value):
	with open(pinData[pin], 'r+') as pin_file:
		pin_file.write(str(value))

def analog(pin):
	with open(adcFiles[pin], 'r') as pin_file:
		pin_file.seek(0)
		return int(pin_file.read(16).split(':')[1])

setup()
while True:
	for i in [0, 1, 7, 5, 4, 2]:
		set(i, 1)
		delay = float(analog(5))/4096
		#print '%0.3f' % delay
		time.sleep(delay)
		set(i, 0)
