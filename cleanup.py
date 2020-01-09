# Add GPIO in-/outputs to file

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # button
GPIO.setup(13, GPIO.OUT)                           # Red led
GPIO.setup(15, GPIO.OUT)                         # Green led
GPIO.setwarnings(False)

print("Cleaning up GPIO pins...")
GPIO.cleanup([11, 13, 15])
