import serial

gps = serial.Serial("/dev/ttyUSB0", baudrate=4800)

for i in range(0,10):
    line = str(gps.readline(), 'utf-8')
    print(line)
