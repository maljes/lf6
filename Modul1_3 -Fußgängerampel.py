#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    LF6-TW1.2 | Modul 1 | Aufgabe 3 & 3a
    von Lidia Machnik, Malte Jesgarzewsky, Dominik Naumann & Marcel Schmager
'''

import RPi.GPIO as GPIO
import time
import sys

#Variablen festlegen
LED_RED = 16
LED_YELLOW = 20
LED_GREEN = 21
LED_RED_2 = 23
LED_GREEN_2 = 24
SWITCH_1 = 13
SWITCH_2 = 19
DELAY = 1
IS_PRESSED = False

def setup():
    GPIO.setmode(GPIO.BCM) # GPIO-Nummer verwenden
    GPIO.setwarnings(False) # Warnungen ausschalten
    GPIO.setup(LED_RED, GPIO.OUT) # Pin als Ausgang verwenden
    GPIO.setup(LED_YELLOW, GPIO.OUT) # Pin als Ausgang verwenden
    GPIO.setup(LED_GREEN, GPIO.OUT) # Pin als Ausgang verwenden
    GPIO.setup(LED_RED_2, GPIO.OUT) # Pin als Ausgang verwenden
    GPIO.setup(LED_GREEN_2, GPIO.OUT) # Pin als Ausgang verwenden
    GPIO.setup(SWITCH_1, GPIO.IN) # Pin als Eingang verwenden
    GPIO.setup(SWITCH_2, GPIO.IN) # Pin als Eingang verwenden
    GPIO.output(LED_RED, GPIO.HIGH) # LED einschalten
    GPIO.output(LED_YELLOW, GPIO.HIGH) # LED ausschalten
    GPIO.output(LED_GREEN, GPIO.HIGH) # LED ausschalten
    GPIO.output(LED_RED_2, GPIO.HIGH) # LED einschalten
    GPIO.output(LED_GREEN_2, GPIO.HIGH) # LED ausschalten
    GPIO.add_event_detect(SWITCH_2, GPIO.RISING, callback=set_pressed)

def destroy():
    GPIO.cleanup() # RESET, GPIO-Pins freigeben
    sys.exit()

def set_pressed(channel):
    global IS_PRESSED
    IS_PRESSED = True
    print 'Signalanforderung durch Fußgänger!'

def dorf():
    global IS_PRESSED
    time.sleep(3)
    while True:
        if IS_PRESSED == True:
            time.sleep(3)
            GPIO.output(LED_GREEN, GPIO.HIGH)
            GPIO.output(LED_YELLOW, GPIO.LOW)
            time.sleep(3)
            GPIO.output(LED_YELLOW, GPIO.HIGH)
            GPIO.output(LED_RED, GPIO.LOW)
            time.sleep(3)
            GPIO.output(LED_RED, GPIO.LOW)
            GPIO.output(LED_RED_2, GPIO.HIGH)
            GPIO.output(LED_GREEN_2, GPIO.LOW)
            time.sleep(15)
            GPIO.output(LED_RED_2, GPIO.LOW)
            GPIO.output(LED_GREEN_2, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(LED_RED, GPIO.LOW)
            GPIO.output(LED_YELLOW, GPIO.LOW)
            time.sleep(3)
            GPIO.output(LED_RED, GPIO.HIGH)
            GPIO.output(LED_YELLOW, GPIO.HIGH)
            GPIO.output(LED_GREEN, GPIO.LOW)
            IS_PRESSED = False
        else:
            GPIO.output(LED_GREEN, GPIO.LOW)
            GPIO.output(LED_RED_2, GPIO.LOW)


def loop():
    global IS_PRESSED
    time.sleep(3)
    GPIO.output(LED_RED, GPIO.LOW)
    GPIO.output(LED_RED_2, GPIO.LOW)
    while True:
        if IS_PRESSED == True:
            print 'Fußgängerampel startet Durchlauf.'
            time.sleep(3)
            GPIO.output(LED_RED, GPIO.LOW)
            GPIO.output(LED_RED_2, GPIO.HIGH)
            GPIO.output(LED_GREEN_2, GPIO.LOW)
            time.sleep(15)
            GPIO.output(LED_RED_2, GPIO.LOW)
            GPIO.output(LED_GREEN_2, GPIO.HIGH)
            time.sleep(3)
            IS_PRESSED = False
        else:
            GPIO.output(LED_RED_2, GPIO.LOW)
            time.sleep(5)

        print 'Autoampel startet Durchlauf.'
        GPIO.output(LED_RED, GPIO.LOW)
        GPIO.output(LED_YELLOW, GPIO.LOW)
        time.sleep(3)
        GPIO.output(LED_RED, GPIO.HIGH)
        GPIO.output(LED_YELLOW, GPIO.HIGH)
        GPIO.output(LED_GREEN, GPIO.LOW)
        time.sleep(15)
        GPIO.output(LED_GREEN, GPIO.HIGH)
        GPIO.output(LED_YELLOW, GPIO.LOW)
        time.sleep(3)
        GPIO.output(LED_YELLOW, GPIO.HIGH)
        GPIO.output(LED_RED, GPIO.LOW)

if __name__ == '__main__': # Programmstart
    setup()
    print 'Programm mit CTRL-C beenden.'
    try:
        #loop()
        dorf()
    except KeyboardInterrupt: # wenn 'CTRL-C' gedrückt, dann Ende
        destroy()
