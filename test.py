import serial
import csv
import time

gps = serial.Serial("/dev/ttyUSB0", baudrate=4800, timeout=5)
status = True
conv_f = 1.852
DEFAULT_VALUE = 0.0
index = int(0)


def gps_speed(data, index):
    line = str(data.readline(), 'ASCII')
    data_line = line.split(',')
    if data_line[0] == '$GPRMC':
        speed = data_line[7]
        print("{}:  {} km/h".format(index, speed))

        
while status:
    try:
        gps_speed(gps, index)
        index += 1
    except UnicodeDecodeError:
        gps_speed(gps, index)
        index += 1
