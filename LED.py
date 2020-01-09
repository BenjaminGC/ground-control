import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.IN)
GPIO.setup(11, GPIO.OUT)

try:
    while True: # Run forever
        if GPIO.input(13) == GPIO.HIGH:
            GPIO.output(11, True)
except KeyboardInterrupt:
    GPIO.cleanup()
