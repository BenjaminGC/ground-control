import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        output = GPIO.input(13)
        if output != 0:
            print('Hello World')
        else:
            pass
except KeyboardInterrupt:
    GPIO.cleanup()

