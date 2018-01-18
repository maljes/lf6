#!/usr/bin/python
# -*- coding: utf-8 -*-

''' Aufgabenstellung
Blinklichter werden oft als Warnung bei gefährlichen
Vorgängen eingesetzt.
Beim Start soll die LED blinken.
Schaltungsaufbau: Variante A
'''

import RPi.GPIO as GPIO # GPIO-Bibliothek
# oder "from RPi import GPIO"
import time # wird für sleep benötigt -> time.sleep(0.5)
# oder "from time import sleep" -> sleep(0.5)
import sys
import os
import math


#Variablen festlegen
LED_RED = 16
LED_YELLOW = 20
LED_GREEN = 21
DELAY = 3

def setup():
    GPIO.setmode(GPIO.BCM) # GPIO-Nummer verwenden
    GPIO.setwarnings(False) # Warnungen ausschalten
    GPIO.setup(LED_RED, GPIO.OUT) # Pin als Eingang verwenden
    GPIO.setup(LED_YELLOW, GPIO.OUT) # Pin als Eingang verwenden
    GPIO.setup(LED_GREEN, GPIO.OUT) # Pin als Eingang verwenden
    GPIO.output(LED_RED, GPIO.HIGH) # LED ausschalten
    GPIO.output(LED_YELLOW, GPIO.HIGH) # LED ausschalten
    GPIO.output(LED_GREEN, GPIO.HIGH) # LED ausschalten

def destroy():
    GPIO.cleanup() # RESET, GPIO-Pins freigeben
    sys.exit()

def loop():
    x = 0
    while True:
        s = os.statvfs('/')
        free = s.f_bsize * s.f_bavail / 1048576
        space = s.f_bsize * s.f_blocks / 1048576
        used = space - free
        perc = float(used) / space
        perc = int(100-perc*100)

        if x != perc:
            print perc,'% frei'
            x = perc

        if perc < 20:
            GPIO.output(LED_RED, GPIO.LOW)
            GPIO.output(LED_YELLOW, GPIO.HIGH)
            GPIO.output(LED_GREEN, GPIO.HIGH)

        if perc >= 20 and perc < 40:
            GPIO.output(LED_RED, GPIO.LOW)
            GPIO.output(LED_YELLOW, GPIO.LOW)
            GPIO.output(LED_GREEN, GPIO.HIGH)

        if perc >= 40 and perc <= 50:
            GPIO.output(LED_RED, GPIO.HIGH)
            GPIO.output(LED_YELLOW, GPIO.LOW)
            GPIO.output(LED_GREEN, GPIO.HIGH)

        if perc > 50 and perc < 80:
            GPIO.output(LED_RED, GPIO.HIGH)
            GPIO.output(LED_YELLOW, GPIO.LOW)
            GPIO.output(LED_GREEN, GPIO.LOW)

        if perc > 80:
            GPIO.output(LED_RED, GPIO.HIGH)
            GPIO.output(LED_YELLOW, GPIO.HIGH)
            GPIO.output(LED_GREEN, GPIO.LOW)

        time.sleep(DELAY)


if __name__ == '__main__': # Programmstart
    setup()
    print 'Programm mit CTRL-C beenden.'
    try:
        loop()
    except KeyboardInterrupt: # wenn 'CTRL-C' gedrückt, dann Ende
        destroy()
