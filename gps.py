import serial

gps = serial.Serial("/dev/ttyUSB0", baudrate=4800)

for i in range(1,10):
    line = gps.readline()
    data_line = line.decode()
    print(data_line)
