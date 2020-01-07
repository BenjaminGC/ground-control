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
            print("Running Program")
        elif self.status:
            self.status = False
            print("Stopping Program")


def update_status():
    running.update()
    print("Changed status")


running = State(False)
GPIO.add_event_detect(13, GPIO.RISING, callback=update_status)

message = input("Press enter to quit\n\n")


GPIO.cleanup()
