#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    LF6-TW1.2 | Modul 1 | Aufgabe 5
    von Lidia Machnik, Malte Jesgarzewsky, Dominik Naumann & Marcel Schmager
'''

import RPi.GPIO as GPIO                                                 # GPIO-Bibliothek
import time                                                             # wird für sleep benötigt -> time.sleep(0.5)
import sys                                                              # wird für sys.exit benötigt
import os                                                               # wird für os.statvfs benötigt

#Variablen festlegen
LED_RED = 16
LED_YELLOW = 20
LED_GREEN = 21
DELAY = 3

def setup():
    GPIO.setmode(GPIO.BCM)                                              # GPIO-Nummer verwenden
    GPIO.setwarnings(False)                                             # Warnungen ausschalten
    GPIO.setup(LED_RED, GPIO.OUT)                                       # Pin als Ausgang verwenden
    GPIO.setup(LED_YELLOW, GPIO.OUT)
    GPIO.setup(LED_GREEN, GPIO.OUT)
    GPIO.output(LED_RED, GPIO.HIGH)                                     # LED ausschalten
    GPIO.output(LED_YELLOW, GPIO.HIGH)
    GPIO.output(LED_GREEN, GPIO.HIGH)

def destroy():
    GPIO.cleanup()                                                      # RESET, GPIO-Pins freigeben
    sys.exit()

def loop():
    x = 0
    while True:
        s = os.statvfs('/')                                             # Daten über den bei '/' gemounteten Speicher abrufen
        free = s.f_bsize * s.f_bavail / 1048576                         # Freien Speicherplatz berechnen
        space = s.f_bsize * s.f_blocks / 1048576                        # Gesamtspeicherplatz berechnen
        used = space - free                                             # Benutzten Speicherplatz berechnen
        perc = float(used) / space                                      # Prozentsatz berechnen
        perc = int(100-perc*100)

        if x != perc:
            print perc,'% frei'
            x = perc

        if perc < 20:                                                   # Überprüfen ob der Prozensatz kleiner als 20 ist
            GPIO.output(LED_RED, GPIO.LOW)
            GPIO.output(LED_YELLOW, GPIO.HIGH)
            GPIO.output(LED_GREEN, GPIO.HIGH)

        if perc >= 20 and perc < 40:                                    # Überprüfen ob der Prozensatz größer als 20 und kleiner als 40 ist
            GPIO.output(LED_RED, GPIO.LOW)
            GPIO.output(LED_YELLOW, GPIO.LOW)
            GPIO.output(LED_GREEN, GPIO.HIGH)

        if perc >= 40 and perc <= 50:                                   # Überprüfen ob der Prozensatz größer als 40 und kleiner als 50 ist
            GPIO.output(LED_RED, GPIO.HIGH)
            GPIO.output(LED_YELLOW, GPIO.LOW)
            GPIO.output(LED_GREEN, GPIO.HIGH)

        if perc > 50 and perc < 80:                                     # Überprüfen ob der Prozensatz größer als 50 und kleiner als 80 ist
            GPIO.output(LED_RED, GPIO.HIGH)
            GPIO.output(LED_YELLOW, GPIO.LOW)
            GPIO.output(LED_GREEN, GPIO.LOW)

        if perc > 80:                                                   # Überprüfen ob der Prozensatz größer als 80 ist
            GPIO.output(LED_RED, GPIO.HIGH)
            GPIO.output(LED_YELLOW, GPIO.HIGH)
            GPIO.output(LED_GREEN, GPIO.LOW)

        time.sleep(DELAY)


if __name__ == '__main__':                                              # Programmstart
    setup()
    print 'Programm mit CTRL-C beenden.'
    try:
        loop()
    except KeyboardInterrupt:                                           # wenn 'CTRL-C' gedrückt, dann Ende
        destroy()
