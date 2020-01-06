import serial

gps = serial.Serial("/dev/ttyUSB0", baudrate=9600)

while True:
    line = gps.readline()
    print(line)
