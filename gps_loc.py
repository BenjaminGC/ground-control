# Need an accuracy of this: 51.17921 N, 3.07762 E, rounding off at 5 decimals after the ','
# Create 2D numpy matrix with coordinates as x and y indices, if these coordinates are received, the x and y
# coordinates in the 2D numpy array will get a value of 1 (0 or 1 available)
# ((x, y), True/False) stored in every a, b of 2D np array, with x and y real coordinates


import serial
import subprocess as sp

gps = serial.Serial("/dev/ttyUSB0", baudrate=4800, timeout=5)
status = True
index = int(1)  # in seconds


def gps_loc(gps):
    global index
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

            lat = round(lat, 5)
            lon = round(lon, 5)     # Accurate enough

            sp.call('clear', shell=True)
            print("{}: LAT= {}, LON= {}".format(index, lat, lon))
            index += int(1)


while status:
    try:
        gps_loc(gps)
    except UnicodeDecodeError:
        gps_loc(gps)
