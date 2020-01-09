import RPi.GPIO as GPIO
import time

LED = 13        # GPIO27
BUTTON = 11     # GPIO17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # button
GPIO.setup(LED, GPIO.OUT)  # led

try:
    while True:
        GPIO.output(LED, GPIO.input(BUTTON))
        time.sleep(1)
except KeyboardInterrupt:
    print("ENDING")
    GPIO.cleanup()
