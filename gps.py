import serial

gps = serial.Serial("/dev/ttyUSB0", baudrate=9600)

for i in range(0, 10):
    line = gps.readline()
    print(line)
