import time
import serial
import numpy as np
import subprocess as sp
import matplotlib.pyplot as plt

gps = serial.Serial("/dev/ttyUSB0", baudrate=4800, timeout=5)
satellites = {}
index = 0


def sat_data(gps):
    global satellites
    try:
        line = str(gps.readline(), 'ASCII')
        data = line.split(',')
        if data[0] == '$GPGSV':
            checksum_data = data[-1].split('*')[1].split('\r')[0]
            data[-1] = data[-1].split('*')[0]
            data.append(checksum_data)
            data = data[4:-1]
            n_sats = int(len(data) / 4)
            for i in range(n_sats):
                name = int(data[i * 4])
                name_data = data[i * 4:(i * 4) + 4]
                for e in range(len(name_data)):
                    if name_data[e] == '':  # if SNR = '' => sat is out of sight but connected
                        name_data[e] = 0
                    else:  # make all other values integers
                        name_data[e] = int(name_data[e])
                satellites[name] = name_data  # Creating satellite dictionary
            return satellites
    except UnicodeError:
        pass


def color_list(e):
    col = []
    for i in range(len(e)):
        col.append(tuple((e[i], 0, 1)))
    return col


def plot(inp):
    try:
        global index
        dict_values = np.array(list(inp.values()), dtype=int)
        sats = np.array(dict_values[:, 0], dtype=str)
        r = dict_values[:, 1]
        theta = np.deg2rad(dict_values[:, 2])
        snr = np.round(dict_values[:, 3] / np.amax(dict_values[:, 3]), 3)
        color = color_list(snr)

        fig = plt.figure()

        ax = fig.add_subplot(111, projection='polar')

        ax.scatter(theta, r, c=color)

        # for i, txt in enumerate(sats):
            # ax.annotate(txt, (theta[i], r[i]))
            
        ax.set_theta_zero_location('N')
        ax.set_theta_direction(-1) 
        ax.set_xticks(np.arange(0, 2.0 * np.pi, np.pi / 18.0))
        ax.set_ylim(90, 0)
        ax.set_yticks(np.arange(0, 90, 10))
        ax.axes.yaxis.set_ticklabels([])

        plt.savefig("sats_{}.png".format(index), bbox_inches='tight')
        index += 1
    except IndexError:
        pass


while True:
    try:
        sat_data(gps)
        # sp.call('clear', shell=True)
        print("{}:{}:{}".format(time.localtime()[3], time.localtime()[4], time.localtime()[5]))
        for key, value in satellites.items():
            print("Satellite {}: elevation = {}, azimuth = {}, SNR = {}".format(key, value[1], value[2], value[3]))
        plot(satellites)
    except KeyboardInterrupt:
        break

# https://github.com/BenjaminGC/ground-control.git
