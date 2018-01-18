#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    LF6-TW1.2 | Modul 1 | Aufgabe 4
    von Lidia Machnik, Malte Jesgarzewsky, Dominik Naumann & Marcel Schmager
'''

import RPi.GPIO as GPIO                                         # GPIO-Bibliothek
import time                                                     # wird für sleep benötigt -> time.sleep(0.5)
import sys                                                      # wird für sys.exit benötigt

#Variablen festlegen
SWITCH_1 = 13
SWITCH_2 = 6
SWITCH_3 = 19
LED_RED = 23
LED_GREEN = 24

def setup():
    GPIO.setmode(GPIO.BCM)                                      # GPIO-Nummer verwenden
    GPIO.setwarnings(False)                                     # Warnungen ausschalten
    GPIO.setup(SWITCH_1, GPIO.IN)                               # Pin als Eingang verwenden
    GPIO.setup(SWITCH_2, GPIO.IN)
    GPIO.setup(SWITCH_3, GPIO.IN)
    GPIO.setup(LED_RED, GPIO.OUT)                               # Pin als Ausgang verwenden
    GPIO.setup(LED_GREEN, GPIO.OUT)
    GPIO.output(LED_RED, GPIO.HIGH)                             # LED ausschalten
    GPIO.output(LED_GREEN, GPIO.HIGH)

def destroy():
    GPIO.cleanup()                                              # RESET, GPIO-Pins freigeben
    sys.exit()

def loop():
    cars = 0
    trucks = 0
    while True:
        car = GPIO.input(SWITCH_1)                              # Status auslesen
        truck = GPIO.input(SWITCH_2)
        reset = GPIO.input(SWITCH_3)

        if car == True:                                         # Status überprüfen
            cars += 1                                           # Variable um eins erhöhen
            print 'Autos: ', cars, ' / LKWs: ', trucks
            GPIO.output(LED_GREEN, GPIO.LOW)                    # LED einschalten
            time.sleep(0.25)                                    # 0.25 Sekunden abwarten
            GPIO.output(LED_GREEN, GPIO.HIGH)                   # LED ausschalten

        if truck == True:
            trucks += 1
            print 'Autos: ', cars, ' / LKWs: ', trucks
            GPIO.output(LED_GREEN, GPIO.LOW)
            time.sleep(0.25)
            GPIO.output(LED_GREEN, GPIO.HIGH)

        if reset == True:
            print 'System schaltet aus.'
            GPIO.output(LED_RED, GPIO.LOW)
            time.sleep(2)
            destroy()

if __name__ == '__main__':                                      # Programmstart
    setup()
    print 'Programm mit CTRL-C beenden.'
    try:
        loop()
    except KeyboardInterrupt:                                   # wenn 'CTRL-C' gedrückt, dann Ende
        destroy()