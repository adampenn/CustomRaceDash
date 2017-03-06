import serial

ser = serial.Serial('/dev/ttyACM0',9600)
s = [0]
while True:
	s[0] = int (ser.readline())
	print(s[0])
