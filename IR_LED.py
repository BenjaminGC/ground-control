import RPi.GPIO as GPIO
import time

IR_LED = 13        # GPIO27
status = False

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)   # led

GPIO.output(LED, True)
print("IR led ON")
time.sleep(5)
GPIO.output(LED, False)
print("IR led OFF")
GPIO.cleanup()
