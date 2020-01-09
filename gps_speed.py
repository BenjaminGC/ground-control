import serial
import csv
import RPi.GPIO as GPIO
import time

gps = serial.Serial("/dev/ttyUSB0", baudrate=4800, timeout=5)
status = True
conv_f = 1.852
DEFAULT_VALUE = 0.0


def gps_speed(data):
    line = str(data.readline(), 'ASCII')
    data_line = line.split(',')
    if data_line[0] == '$GPRMC':
        speed = float(data_line[7])*conv_f
        if speed <= 1.5:
            speed = 0.0
        else:
            pass
        return speed


GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

with open('speed.csv', 'w', newline='') as file:
    GPIO.output(15, True)
    file_writer = csv.writer(file)
    for i in range(0, 25):
        try:
            GPIO.output(13, True)
            speed = gps_speed(gps)
            if speed is None:
                speed = DEFAULT_VALUE
            print("Speed: {} km/h".format(speed))
            file_writer.writerow([float(speed)])
            GPIO.output(13, False)
            time.sleep(0.25)
        except UnicodeDecodeError:
            GPIO.output(13, True)
            speed = gps_speed(gps)
            if speed is None:
                speed = DEFAULT_VALUE
            print("Speed: {} km/h".format(speed))
            file_writer.writerow([float(speed)])
            GPIO.output(13, False)
            time.sleep(0.25)
GPIO.cleanup()
