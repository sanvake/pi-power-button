#!/usr/bin/env python


import RPi.GPIO as GPIO
import subprocess
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(3, GPIO.RISING)
sleep(5)
if(GPIO.FALLING):
    subprocess.call(['shutdown', '-h', 'now'], shell=False)
