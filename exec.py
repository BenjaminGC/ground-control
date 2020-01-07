import RPi.GPIO as GPIO


ButtonPin = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        if GPIO.input(11) == 1:
            print(True)
        else:
            print(False)
except KeyboardInterrupt:
    GPIO.cleanup()
