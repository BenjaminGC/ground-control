import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        print(GPIO.input(13))
except KeyboardInterrupt:
    GPIO.cleanup()

