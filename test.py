import serial

gps = serial.Serial("/dev/ttyUSB0", baudrate=4800, timeout=5)
status = True
conv_f = 1.852


def gps_speed(data):
    line = str(data.readline(), 'ASCII')
    data_line = line.split(',')
    if data_line[0] == '$GPRMC':
        speed = float(data_line[7])*conv_f
        print("Speed: {} km/h".format(speed))


while status:
    gps_speed(gps)
