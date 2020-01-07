import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN)

try:
    while True: # Run forever
        if GPIO.input(13) == GPIO.HIGH:
            print("Button was pushed!")
except KeyboardInterrupt:
    GPIO.cleanup()

