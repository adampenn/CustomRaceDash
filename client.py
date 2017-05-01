#!/usr/bin/python3

import socket

serverAddress = 'b8:27:eb:7b:60:24'

port = 3

s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverAddress,port))

while True:
  text = input();
  if text == "quit":
    break
  s.send(bytes(text, 'UTF-8'))
s.close()

