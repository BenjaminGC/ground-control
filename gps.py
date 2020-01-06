import serial

gps = serial.Serial("/dev/ttyUSB0", baudrate=4800)

while True:
    line = gps.readline()
    data = line.split(",")
    print(data, len(data))
