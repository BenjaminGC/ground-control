import RPi.GPIO as GPIO
import time

LED = 15
BUTTON = 13

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, False)

class Push:
    @staticmethod
    def button_callback():
        global LED, BUTTON
        GPIO.output(LED, GPIO.HIGH)


GPIO.add_event_detect(BUTTON, GPIO.RISING, callback=Push.button_callback)

message = input("Press enter to quit...\n\n")
GPIO.cleanup()
