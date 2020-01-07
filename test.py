import serial
import csv

gps = serial.Serial("/dev/ttyUSB0", baudrate=4800, timeout=5)
status = True
conv_f = 1.852
DEFAULT_VALUE = 0.0


def gps_speed(data):
    line = str(data.readline(), 'ASCII')
    data_line = line.split(',')
    if data_line[0] == '$GPRMC':
        speed = data_line[7]
        if speed is None:
            speed = DEFAULT_VALUE
        speed = speed*conv_f
        if speed <= 1.5:
            speed = 0.0
        else:
            pass
        print("Speed: {} km/h".format(speed))
