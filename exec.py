import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


class State:

    def __init__(self, status):
        self.status = status

    def update(self):
        if not self.status:
            self.status = True

        elif self.status:
            self.status = False


message = input("Press enter to quit\n\n")

running = State(False)
print("To start program, press button...")
GPIO.add_event_detect(13, GPIO.RISING, callback=running.update())
print("Program terminated")

GPIO.cleanup()
