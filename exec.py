import RPi.GPIO as GPIO

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

try:
    while True: # Run forever
        if GPIO.input(13) == GPIO.HIGH:
            print("Button was pushed!")
except KeyboardInterrupt:
    GPIO.cleanup()

