import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        if GPIO.input(13) == 1:
            print(True)
        else:
            print(False)
except KeyboardInterrupt:
    GPIO.cleanup()

