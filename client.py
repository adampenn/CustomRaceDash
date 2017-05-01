#!/usr/bin/python3

import bluetooth

serverMACAddress = 'b8:27:eb:7b:60:24'
port = 3
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))
while 1:
    text = raw_input() # Note change to the old (Python 2) raw_input
    if text == "quit":
    break
    s.send(text)
sock.close()
