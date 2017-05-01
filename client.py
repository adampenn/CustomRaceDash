#!/usr/bin/python3.3

import socket

#serverMACAddress = 'b8:27:eb:2d:17:5a'
serverMACAddress = 'b8:27:eb:7b:60:24'
port = 3
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))
while 1:
    text = input()
    if text == "quit":
        break
    s.send(bytes(text, 'UTF-8'))
s.close()
