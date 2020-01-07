import RPi.GPIO as GPIO

status = False

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def button_callback(status):
    print("Status: {}".format(status))
    if status == False:
        status = True
    elif status == True:
        status = False
    print("Status changed to: {}".format(status))
    return status
    

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


GPIO.add_event_detect(13,GPIO.RISING,callback=exec)

message = input("Press enter to quit\n\n")

GPIO.cleanup()
