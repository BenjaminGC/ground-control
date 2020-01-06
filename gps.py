import serial

gps = serial.Serial("/dev/ttyUSB0", baudrate=4800)


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
    else:
        pass


def gps_speed(data):
    line = str(data.readline(), 'ASCII')
    data_line = line.split(',')
    if data_line[0] == '$GPVTG':
        speed = str(data_line[7].replace('.', ',') + '\1km/h')
        print('Speed: {}'.format(speed))
        print('\n')


for i in range(0, 20):
    try:
        gps_data(gps)
        gps_speed(gps)
    except UnicodeDecodeError:
        gps_data(gps)
        gps_speed(gps)
