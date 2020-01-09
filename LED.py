import RPi.GPIO as GPIO
import time

LED = 13        # GPIO27
BUTTON = 11     # GPIO17

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # button
GPIO.setup(LED, GPIO.OUT)  # led

try:
    while True:
        button_input = GPIO.input(BUTTON)
        GPIO.output(LED, button_input)
        print(button_input)
        #time.sleep(1)
except KeyboardInterrupt:
    print("ENDING")
    GPIO.cleanup()
