#!/usr/bin/python3

import socket

serverAddress = 'b8:27:eb:2d:17:5a'

port = 3

s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))

while True:
  text = input();
  if text == ""quit":
    break
  s.send(bytes(text, 'UTF-8'))
s.close()

