import RPi.GPIO as GPIO
import time
import serial
import csv
import subprocess as sp

LED_RED = 13    # GPIO27
LED_GREEN = 15  # GPIO22
BUTTON = 11     # GPIO17
status = False
gps = serial.Serial("/dev/ttyUSB0", baudrate=4800, timeout=5)
conv_f = 1.852
DEFAULT_VALUE = 0.0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # button
GPIO.setup(LED_RED, GPIO.OUT)                           # Red led
GPIO.setup(LED_GREEN, GPIO.OUT)                         # Green led

GPIO.output([LED_GREEN, LED_RED], False)
sp.call('clear', shell=True)


def speed(data):
    line = str(data.readline(), 'ASCII')
    data_line = line.split(',')
    if data_line[0] == '$GPRMC':
        v = float(data_line[7])*conv_f
        if v <= 1.5:
            v = 0.0
        else:
            pass
        if v is None:
            v = DEFAULT_VALUE
        print("Speed: {} km/h".format(v))
        return v


def gps_speed():
    with open('speed.csv', 'w', newline='') as file:
        file_writer = csv.writer(file)
        while status:
            try:
                global status
                button_inp = not bool(GPIO.input(BUTTON))
                GPIO.output(LED_GREEN, True)
                velocity = speed(gps)
                file_writer.writerow([float(velocity)])
                GPIO.output(LED_GREEN, False)
                if button_inp and status:
                    status = False
                    sp.call('clear', shell=True)
                    print("Ending program")
                time.sleep(1)
            except UnicodeDecodeError:
                global status
                button_inp = not bool(GPIO.input(BUTTON))
                GPIO.output(LED_GREEN, True)
                velocity = speed(gps)
                file_writer.writerow([float(velocity)])
                GPIO.output(LED_GREEN, False)
                if button_inp and status:
                    status = False
                    sp.call('clear', shell=True)
                    print("Ending program")
                time.sleep(1)


try:
    if not status:
        GPIO.output(LED_RED, status)
        while not status:
            button_input = not bool(GPIO.input(BUTTON))
            if button_input and not status:
                status = True
                print("Program running")
                time.sleep(1)
    GPIO.output(LED_RED, status)
    gps_speed()

    GPIO.output(LED_RED, status)
    GPIO.cleanup()

except KeyboardInterrupt:
    GPIO.cleanup()
    print('FORCE QUIT')


# https://github.com/BenjaminGC/ground-control.git
