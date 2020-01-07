import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN)

try:
    while True:
        input_value = GPIO.input(13)
        if input_value == False:
            print('Hello World')
            while input_value == False:
                input_value = GPIO.input(13)
        else:
            pass
except KeyboardInterrupt:
    GPIO.cleanup()

