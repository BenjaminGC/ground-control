import serial

gps = serial.Serial("/dev/ttyUSB0", baudrate=4800, timeout=5)
status = True


def gps_speed(data):
    line = str(data.readline(), 'ASCII')
    data_line = line.split(',')
    if data_line[0] == '$GPVTG':
        speed = str(data_line[7].replace('.', ',') + '\1km/h')
        print('Speed: {}'.format(speed))
    else:
        pass


while status:
    try:
        gps_speed(gps)
    except UnicodeDecodeError:
        gps_speed(gps)
