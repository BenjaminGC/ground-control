import serial

gps = serial.Serial("/dev/ttyUSB0", baudrate=4800)

for i in range(0,10):
    line = str(gps.readline(), 'ASCII')
    data_line = line.split(',')
    print(data_line)
