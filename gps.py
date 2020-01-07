import serial
import csv
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

gps = serial.Serial("/dev/ttyUSB0", baudrate=4800, timeout=5)
status = True
conv_f = 1.852
DEFAULT_VALUE = 0.0


def degrees(pos):
    split_pos = pos.split('.')
    seconds = str((int(split_pos[1])/pow(10, len(split_pos[1])))*60)
    if len(split_pos[0]) == 4:
        minutes = str(split_pos[0][2:])
        hours = str(split_pos[0][0:2])
        location = hours + "°" + minutes + "'" + seconds + '"'
        return location
    elif len(split_pos[0]) == 5:
        minutes = str(split_pos[0][3:])
        hours = str(split_pos[0][0:3])
        location = hours + "°" + minutes + "'" + seconds + '"'
        return location


def gps_loc(data):
    line = str(data.readline(), 'ASCII')
    data_line = line.split(',')
    if data_line[0] == '$GPGGA':
        local_time = data_line[1][:6]
        local_time = str("{}:{}:{}".format(local_time[0:2], local_time[2:4], local_time[4:6]))
        lat = str(degrees(data_line[2]) + data_line[3])
        lon = str(degrees(data_line[4]) + data_line[5])
        altitude = data_line[9]
        satellites_in_use = data_line[7]
        print('Local Time (SH): {} Z, Latitude: {}, Longitude: {}, Altitude (MSL): {}'.format(local_time
                                                                                                  , lat
                                                                                                  , lon
                                                                                                  , altitude))
        print('Satellites in use: {}'.format(satellites_in_use))
        print('-----------------------------------------------------------------------------------------------'
              '-----------------------------------------------------------------')
    else:
        pass


def speed(data):
    line = str(data.readline(), 'ASCII')
    data_line = line.split(',')
    if data_line[0] == '$GPRMC':
        speed = float(data_line[7])*conv_f
        if speed <= 1.5:
            speed = 0.0
        else:
            pass
        if speed is None:
            speed = DEFAULT_VALUE
        print("Speed: {} km/h".format(speed))
        return speed


def gps_speed():
    with open('speed.csv', 'w', newline='') as file:
        GPIO.output(7, True)
        file_writer = csv.writer(file)
        for i in range(0, 25):
            try:
                GPIO.output(11, True)
                speed = speed(gps)
                file_writer.writerow([float(speed)])
                GPIO.output(11, False)
                time.sleep(1)
            except UnicodeDecodeError:
                GPIO.output(11, True)
                speed = speed(gps)
                file_writer.writerow([float(speed)])
                GPIO.output(11, False)
                time.sleep(1)
    GPIO.cleanup()


answer = str(input("Location/Speed? "))
        
while status:
    if answer == 'Speed':
        gps_speed()
    if answer == 'Location':
        try:
            gps_loc(gps)
        except UnicodeDecodeError:
            gps_loc(gps)
    else:
        print('No option chosen')
        pass
