import serial

gps = serial.Serial("/dev/ttyUSB0", baudrate=4800, timeout=5)
status = True


def gps_speed(data):
    line = str(data.readline(), 'ASCII')
    data_line = line.split(',')
    print(data_line[0])


while status:
    gps_speed(gps)
