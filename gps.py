import serial

gps = serial.Serial("/dev/ttyUSB0", baudrate=4800)

for i in range(0, 20):
    line = str(gps.readline(), 'ASCII')
    data_line = line.split(',')
    if data_line[0] == '$GPGGA':
        print('Local Time: {} Z, Latitude: {} {}, Longitude: {} {}, Altitude (ASL): {} \n'.format(data_line[1], data_line[2], data_line[3], data_line[4], data_line[5], data_line[9]))
        print('Satellites in use: {}'.format(data_line[7]))
    else:
        pass
