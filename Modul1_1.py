#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    LF6-TW1.2 | Modul 1 | Aufgabe 1 & 1a
    von Lidia Machnik, Malte Jesgarzewsky, Dominik Naumann & Marcel Schmager
'''

import RPi.GPIO as GPIO                                         # GPIO-Bibliothek
import time                                                     # wird für sleep benötigt -> time.sleep(0.5)
import sys                                                      # wird für sys.exit benötigt

#Variablen festlegen
LED_RED = 16
LED_YELLOW = 20
LED_GREEN = 21
SWITCH_1 = 13
SWITCH_2 = 6
SWITCH_3 = 5
SWITCH_4 = 19
DELAY = 0.30


def setup():
    GPIO.setmode(GPIO.BCM)                                      # GPIO-Nummer verwenden
    GPIO.setwarnings(False)                                     # Warnungen ausschalten
    GPIO.setup(LED_RED, GPIO.OUT)                               # Pin als Ausgang verwenden
    GPIO.setup(LED_YELLOW, GPIO.OUT)
    GPIO.setup(LED_GREEN, GPIO.OUT)
    GPIO.setup(SWITCH_1, GPIO.IN)                               # Pin als Eingang verwenden
    GPIO.setup(SWITCH_2, GPIO.IN)
    GPIO.setup(SWITCH_3, GPIO.IN)
    GPIO.setup(SWITCH_4, GPIO.IN)
    GPIO.output(LED_RED, GPIO.HIGH)                             # LED ausschalten
    GPIO.output(LED_YELLOW, GPIO.HIGH)
    GPIO.output(LED_GREEN, GPIO.HIGH)

def destroy():
    GPIO.cleanup()                                              # RESET, GPIO-Pins freigeben
    sys.exit()

def loop():
    red = 0
    yellow = 0
    green = 0
    while True:
        input_switch1 = GPIO.input(SWITCH_1)                    # Status auslesen
        input_switch2 = GPIO.input(SWITCH_2)
        input_switch3 = GPIO.input(SWITCH_3)
        input_switch4 = GPIO.input(SWITCH_4)

        if  input_switch1 == True:                              # Status überprüfen
            if(red == 0):
                GPIO.output(LED_RED, GPIO.LOW)                  # LED einschalten
                print 'Rot wurde eingeschaltet'
                time.sleep(DELAY)
                red = 1
            else:
                GPIO.output(LED_RED, GPIO.HIGH)                 # LED ausschalten
                print 'Rot wurde ausgeschaltet'
                time.sleep(DELAY)
                red = 0

        if  input_switch2 == True:
            if(yellow == 0):
                GPIO.output(LED_YELLOW, GPIO.LOW)
                print 'Gelb wurde eingeschaltet'
                time.sleep(DELAY)
                yellow = 1
            else:
                GPIO.output(LED_YELLOW, GPIO.HIGH)
                print 'Gelb wurde ausgeschaltet'
                time.sleep(DELAY)
                yellow = 0

        if  input_switch3 == True:
            if(green == 0):
                GPIO.output(LED_GREEN, GPIO.LOW)
                print 'Gruen wurde eingeschaltet'
                time.sleep(DELAY)
                green = 1
            else:
                GPIO.output(LED_GREEN, GPIO.HIGH)
                print 'Gruen wurde ausgeschaltet'
                time.sleep(DELAY)
                green = 0

        if  input_switch4 == True:
            GPIO.output(LED_RED, GPIO.HIGH)
            GPIO.output(LED_YELLOW, GPIO.HIGH)
            GPIO.output(LED_GREEN, GPIO.HIGH)
            print 'Alle lampen wurden ausgeschaltet'
            time.sleep(DELAY)

if __name__ == '__main__':                                      # Programmstart
    setup()
    print 'Programm mit CTRL-C beenden.'
    try:
        loop()
    except KeyboardInterrupt:                                   # wenn 'CTRL-C' gedrückt, dann Ende
        destroy()
