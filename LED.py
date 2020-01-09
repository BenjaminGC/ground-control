import RPi.GPIO as GPIO
import time

LED = 11
BUTTON = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON, GPIO.IN)  # button
GPIO.setup(LED, GPIO.OUT)  # led
GPIO.output(LED, False)     # LED begin state to false


try:
    while True:
        # Turn LED off
        print("LED off")
        GPIO.output(LED, GPIO.LOW)
    
        # waiting for button press
        while GPIO.input(BUTTON) == 1:
            time.sleep(0.2)
    
            # Turn LED on
        print("LED on")
        GPIO.output(LED, GPIO.HIGH)
    
        # waiting for button release
        while GPIO.input(BUTTON) == 0:
            time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
