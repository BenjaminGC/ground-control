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


def run():
    running.status = running.update


running = State(False)
print("To start program, press button...")
GPIO.add_event_detect(13, GPIO.RISING, callback=run)
if running.status:
    print("Program terminated")
else:
    pass

message = input("Press ENTER to quit")

GPIO.cleanup()
