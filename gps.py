import serial

gps = serial.Serial("/dev/ttyUSB0", baudrate=4800)

for i in range(0,10):
    line = gps.readline()
    line = str(line, 'ASCII')
    # data_line = line.split(',')
    print(line)
