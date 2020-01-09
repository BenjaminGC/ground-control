import RPi.GPIO as GPIO

LED = 13        # GPIO27
BUTTON = 11     # GPIO17
status = True

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # button
GPIO.setup(LED, GPIO.OUT)  # led


try:
    GPIO.output(LED, status)
    while status:
        button_input = not GPIO.input(BUTTON)
        if button_input:
            status = False
    GPIO.output(LED, status)
    print(status)
    GPIO.cleanup()
except KeyboardInterrupt:
    GPIO.cleanup()



