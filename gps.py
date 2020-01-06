import serial

gps = serial.Serial("/dev/ttyUSB0", baudrate=9600)

print gps
