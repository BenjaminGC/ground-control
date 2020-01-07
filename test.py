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
    return float(v)*conv_f


def elapsed_time(tuple_start, tuple_end):
    list_start = list(tuple_start)
    list_end = list(tuple_end)
    list_elapsed_time = [int(list_end[0]-list_start[0]),
                         int(list_end[1]-list_start[1]),
                         int(list_end[2]-list_start[2])]
    return list_elapsed_time

try:
    start_time = time.localtime()[3:6]
    print("Time at start: {}:{}:{}".format(start_time[0], start_time[1], start_time[2]))
    while status:
        try:
            speed = gps_speed(gps)
            speed = conv(speed)
            print("{}: {} km/h".format(index, speed))
            index += 1
        except UnicodeDecodeError:
            speed = gps_speed(gps)
            speed = conv(speed)
            print("{}: {} km/h".format(index, speed))
            index += 1
except KeyboardInterrupt:       # ctrl+c
    end_time = time.localtime()[3:6]
    print("Time at end: {}:{}:{}".format(end_time[0], end_time[1], end_time[2]))
    elapsed_time = elapsed_time(start_time, end_time)
    print("Elapsed time: {}:{}:{}".format(elapsed_time[0], elapsed_time[1], elapsed_time[2]))

    
