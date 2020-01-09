import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
print("Cleaning up GPIO pins...")
GPIO.cleanup([11, 13, 15])
