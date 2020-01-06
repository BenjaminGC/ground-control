import serial
import csv

gps = serial.Serial("/dev/ttyUSB0", baudrate=4800, timeout=5)
status = True
conv_f = 1.852


def gps_speed(data):
    line = str(data.readline(), 'ASCII')
    data_line = line.split(',')
    if data_line[0] == '$GPRMC':
        speed = float(data_line[7])*conv_f
        if speed <= 1.0:
            speed = 0
        else:
            pass
        return speed


with open('speed.csv', 'w', newline='') as file:
    file_writer = csv.writer(file)
    for i in range(0, 25):
        try:
            file_writer.writerow(gps_speed(gps))
        except UnicodeDecodeError:
            file_writer.writerow(gps_speed(gps))
