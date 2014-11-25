#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

from pibell.sim900 import Sim900

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def call():
    number = ""
    sim900 = Sim900()
    sim900.call(number)


while True:
    input_state = GPIO.input(21)
    if input_state == False:
        print('Putton bressed!')
        call()
        time.sleep(0.2)
