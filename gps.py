import serial

gps = serial.Serial("/dev/ttyUSB0", baudrate=4800)

for i in range(0,10):
    line = gps.readline()
    #data_line = line.decode('b')
    print(line)
