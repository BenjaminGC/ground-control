import serial

gps = serial.Serial("/dev/ttyUSB0", baudrate=4800, timeout=5)
status = True
conv_f = 1.852


def gps_speed(data):
    with open('speed.txt', 'w') as file:
        line = str(data.readline(), 'ASCII')
        data_line = line.split(',')
        if data_line[0] == '$GPRMC':
            speed = float(data_line[7])*conv_f
            if speed <= 1.0:
                speed = 0
            else:
                pass
            print("Speed: {} km/h".format(speed))
            file.write(str(speed))


for i in range(0, 25):
    try:
        gps_speed(gps)
    except UnicodeDecodeError:
        gps_speed(gps)
