import RPi.GPIO as GPIO

print("Cleaning up GPIO pins...")
GPIO.cleanup([11, 13, 15])
