#!/usr/bin/python3/3

import socket
import pickle

#hostMACAddress = 'b8:27:eb:2d:17:5a'
hostMACAddress = 'b8:27:eb:7b:60:24'
port = 3 # 3 is an arbitrary choice. However, it must match the port used by the client.
backlog = 1
size = 4096
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((hostMACAddress,port))
s.listen(backlog)
client, address = s.accept()
print('Connected by', address)
while 1:
  data = client.recv(size)
  if data:
    print(data.decode("utf-8"))
    client.send(data)

print("Closing socket")	
client.close()
s.close()
