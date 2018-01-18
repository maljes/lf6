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

#Variablen festlegen
LED_1 = 16
SWITCH_1 = 13
DELAY = 1

def setup():
    GPIO.setmode(GPIO.BCM) # GPIO-Nummer verwenden
    GPIO.setwarnings(False) # Warnungen ausschalten
    GPIO.setup(LED_1, GPIO.OUT) # Pin als Ausgang verwenden
    GPIO.setup(SWITCH_1, GPIO.IN) # Pin als Ausgang verwenden

def destroy():
    GPIO.cleanup() # RESET, GPIO-Pins freigeben
    sys.exit()

def loop():
    running = 0
    while True:
        input_value = GPIO.input(SWITCH_1)  # Status auslesen
        if input_value == True:
            if running == 0:
                running = 1
                print 'Taster gedrückt -> Läuft'
            else:
                running = 0
                print 'Taster gedrückt -> Läuft nicht'

        if running == 0:
            GPIO.output(LED_1, GPIO.HIGH)
            time.sleep(DELAY)
        else:
            GPIO.output(LED_1,GPIO.LOW)
            time.sleep(DELAY)

if __name__ == '__main__': # Programmstart
    setup()
    print 'Programm mit CTRL-C beenden.'
    try:
        loop()
    except KeyboardInterrupt: # wenn 'CTRL-C' gedrückt, dann Ende
        destroy()
