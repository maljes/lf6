#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    LF6-TW1.2 | Modul 1 | Aufgabe 2
    von Lidia Machnik, Malte Jesgarzewsky, Dominik Naumann & Marcel Schmager
'''

import RPi.GPIO as GPIO                                         # GPIO-Bibliothek
import time                                                     # wird für sleep benötigt -> time.sleep(0.5)
import sys                                                      # wird für sys.exit benötigt

#Variablen festlegen
LED_RED = 16
SWITCH_1 = 13
DELAY = 1

def setup():
    GPIO.setmode(GPIO.BCM)                                      # GPIO-Nummer verwenden
    GPIO.setwarnings(False)                                     # Warnungen ausschalten
    GPIO.setup(LED_RED, GPIO.OUT)                               # Pin als Ausgang verwenden
    GPIO.setup(SWITCH_1, GPIO.IN)                               # Pin als Eingang verwenden
    GPIO.output(LED_RED, GPIO.HIGH)                             # LED ausschalten

def destroy():
    GPIO.cleanup()                                              # RESET, GPIO-Pins freigeben
    sys.exit()

def loop():
    while True:
        input_value = GPIO.input(SWITCH_1)                      # Status auslesen
        if input_value == True:                                 # Status überprüfen
            GPIO.output(LED_RED, GPIO.LOW)                      # LED einschalten
            time.sleep(DELAY)                                   # DELAY abwarten
            GPIO.output(LED_RED, GPIO.HIGH)                     # LED ausschalten
            time.sleep(DELAY)

if __name__ == '__main__':                                      # Programmstart
    setup()
    print 'Programm mit CTRL-C beenden.'
    try:
        loop()
    except KeyboardInterrupt:                                   # wenn 'CTRL-C' gedrückt, dann Ende
        destroy()