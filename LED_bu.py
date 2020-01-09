import RPi.GPIO as GPIO
import time
import subprocess as sp

LED = 13        # GPIO27
BUTTON = 11     # GPIO17

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # button
GPIO.setup(LED, GPIO.OUT)  # led

try:
    while True:
        button_input = not GPIO.input(BUTTON)
        if button_input:
            GPIO.output(LED, button_input)
            print("LED ON")
        else:
            GPIO.output(LED, button_input)
            print("LED OFF")
        sp.call('clear', shell=True)
except KeyboardInterrupt:
    print("ENDING")
    GPIO.cleanup()
