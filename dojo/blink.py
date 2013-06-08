#!/usr/bin/env python

"""
Blink:
piscar o ponto decimal no display de 7 segmentos do circuito 'Dojo com pcDuino'
"""

# fonte:
# https://learn.sparkfun.com/tutorials/programming-the-pcduino/accessing-gpio-pins
# https://learn.sparkfun.com/tutorials/programming-the-pcduino/analog-input-and-output

import time, os, sys

GPIO_MODE_PATH= os.path.normpath('/sys/devices/virtual/misc/gpio/mode/')
GPIO_PIN_PATH=os.path.normpath('/sys/devices/virtual/misc/gpio/pin/')

HIGH = "1"
LOW =  "0"
INPUT = "0"
OUTPUT = "1"

def setup():
    with open(pin, 'r+') as f: ## open the file in r/w mode
        f.write(OUTPUT)        ## set the mode of the pin

    with open(pin, 'r+') as f: ## open the file in r/w mode
        f.write(LOW)

def set(pin, value):
    with open(pinData[pin], 'r+') as pin_file:
        pin_file.write(str(value))

setup()
pin = sys.argv[1]
while True:
    set(pin, HIGH)
    sleep(1)
    set(pin, LOW)
