import serial
import time
import subprocess as sp

gps = serial.Serial("/dev/ttyUSB0", baudrate=4800, timeout=5)
status = True


def gps_loc(gps):
    line = str(gps.readline(), 'ASCII')
    data = line.split(",")
    if data[0] == '$GPRMC':
        if data[2] == 'A':

            lat_gps = float(data[3])
            if data[4] == "S":
                lat_gps = -lat_gps

            lat_deg = int(lat_gps / 100)
            lat_min = lat_gps - lat_deg * 100
            lat = lat_deg + (lat_min / 60)

            long_gps = float(data[5])
            if data[4] == "W":
                long_gps = - long_gps

            long_deg = int(long_gps / 100)
            long_min = long_gps - long_deg * 100
            lon = long_deg + (long_min / 60)

            sp.call('clear', shell=True)
            print("LAT: {}\nLON: {}".format(lat, lon))
            time.sleep(0.1)


while status:
    try:
        gps_loc(gps)
    except UnicodeDecodeError:
        gps_loc(gps)
