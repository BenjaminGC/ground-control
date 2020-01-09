import RPi.GPIO as GPIO
import time
import subprocess as sp

LED = 13        # GPIO27
BUTTON = 11     # GPIO17
status = False
i = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # button
GPIO.setup(LED, GPIO.OUT)  # led


def text(number):
    number = number * 4
    return number


def adder():
    global status
    while status:
        global i
        button_inp = not bool(GPIO.input(BUTTON))
        value = text(3)
        i += 1
        print("Outcome is: {}".format(value))
        if button_inp and status:
            status = False
            print("LED OFF\n")
            time.sleep(1)


try:
    if not status:
        GPIO.output(LED, status)
        while not status:
            button_input = not bool(GPIO.input(BUTTON))
            if button_input and not status:
                status = True
                print("LED ON\n")
                time.sleep(1)
    GPIO.output(LED, status)
    adder()
    GPIO.output(LED, status)
    GPIO.cleanup()

except KeyboardInterrupt:
    GPIO.cleanup()
    print('FORCE QUIT')

    
# https://github.com/BenjaminGC/ground-control.git
