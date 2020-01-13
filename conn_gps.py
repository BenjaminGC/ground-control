import serial
import subprocess as sp
import time

gps = serial.Serial("/dev/ttyUSB0", baudrate=4800, timeout=5)
satellites = {}


def sat_data(data):
    global satellites
    try:
        line = str(gps.readline(), 'ASCII')
        data = line.split(',')
        if data[0] == '$GPGSV':
            checksum_data = data[-1].split('*')[1].split('\r')[0]
            data[-1] = data[-1].split('*')[0]
            data.append(checksum_data)
            data = data[4:-1]
            n_sats = int(len(data)/4)
            for i in range(n_sats):
                name = int(data[i*4])
                name_data = data[i*4:(i*4)+4][1:]
                for e in range(len(name_data)):
                    if name_data[e] == '':                  # if SNR = '' => sat is out of sight but connected
                        name_data[e] = 0
                    else:                                   # make all other values integers
                        name_data[e] = int(name_data[e])
                satellites[name] = name_data                # Creating satellite dictionary
            return satellites
    except UnicodeError:
        pass


while True:
    try:
        # sp.call('clear', shell=True)
        sat_data(gps)
        sp.call('clear', shell=True)
        for key, value in satellites.items():
            print("Satellite {}: elevation = {}, azimuth = {}, SNR = {}".format(key, value[0], value[1], value[2]))
        time.sleep(1)
        print("updating..."
        # sp.call('clear', shell=True)
    except KeyboardInterrupt:
        break

        
# https://github.com/BenjaminGC/ground-control.git
