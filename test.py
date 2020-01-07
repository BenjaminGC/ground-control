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
        return speed

    
def conv(v):
    if v is None:
        v = DEFAULT_VALUE
    else:
        pass
    return v*conv_f


try:
    start_time = time.localtime()[3:6]
    print("Time at start: {}:{}:{}".format(start_time[0], start_time[1], start_time[2]))
    while status:
        try:
            speed = gps_speed(gps)
            speed = conv(speed)
            print("{}: {} km/h".format(index, speed))
        except UnicodeDecodeError:
            speed = gps_speed(gps)
            speed = conv(speed)
            print("{}: {} km/h".format(index, speed))
except KeyboardInterrupt:       # ctrl+c
    end_time = time.localtime()[3:6]
    print("Time at end: {}:{}:{}".format(end_time[0], end_time[1], end_time[2]))

    
