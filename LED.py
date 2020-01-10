import RPi.GPIO as GPIO
import time
import subprocess as sp

LED = 13        # GPIO27
BUTTON = 11     # GPIO17
status = False

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # button
GPIO.setup(LED, GPIO.OUT)  # led


try:
    if not status:
        GPIO.output(LED, status)
        while not status:
            button_input = not bool(GPIO.input(BUTTON))
            if button_input and not status:
                status = True
                print("LED ON")
                time.sleep(1)
    print(status)
    GPIO.output(LED, status)
    while status:
        button_input = not bool(GPIO.input(BUTTON))
        if button_input and status:
            status = False
            print("LED OFF")
            time.sleep(1)
    print(status)
    GPIO.output(LED, status)
    GPIO.cleanup()

except KeyboardInterrupt:
    GPIO.cleanup()
    print('FORCE QUIT')

