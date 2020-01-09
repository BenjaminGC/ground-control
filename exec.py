import RPi.GPIO as GPIO
import time
import subprocess as sp

LED = 13        # GPIO27
BUTTON = 11     # GPIO17
status = False

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # button
GPIO.setup(LED, GPIO.OUT)  # led


try:
    while True:
        GPIO.output(LED, status)
        while not status:
            button_input = not GPIO.input(BUTTON)
            if button_input and not status:
                status = True
            elif button_input and status:
                status = False
        GPIO.output(LED, status)
        print(status)
        sp.call('clear', shell=True)
except KeyboardInterrupt:
    GPIO.cleanup()

# https://github.com/BenjaminGC/ground-control.git
