import serial
import csv
import time

gps = serial.Serial("/dev/ttyUSB0", baudrate=4800, timeout=5)
status = True
conv_f = 1.852
DEFAULT_VALUE = 0.0
index = int(0)


def gps_speed(data):
    line = str(data.readline(), 'ASCII')
    data_line = line.split(',')
    if data_line[0] == '$GPRMC':
        speed = data_line[7]
        time.sleep(1)
        return speed

        
while status:
    try:
        speed = gps_speed(gps)
        print("{}: {} km/h".format(index, speed))
        index += 1
    except UnicodeDecodeError:
        speed = gps_speed(gps)
        print("{}: {} km/h".format(index, speed))
        index += 1
