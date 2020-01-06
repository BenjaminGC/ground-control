import serial

gps = serial.Serial("/dev/ttyUSB0", baudrate=4800)

for i in range(0,100):
    line = gps.readline()
    data_line = line.decode()
    if data_line[0] == '$GPGSV':
        print('satellites in view: {}'.format(data_line))
    else:
        pass
