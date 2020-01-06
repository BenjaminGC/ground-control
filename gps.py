import serial

gps = serial.Serial("/dev/ttyUSB0", baudrate=4800)

for i in range(0, 20):
    line = str(gps.readline(), 'ASCII')
    data_line = line.split(',')
    if data_line[0] == '$GPGSV':
        print('Satellites in view: {}'.format(data_line))
    else:
        pass
