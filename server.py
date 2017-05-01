#!/usr/bin/python3/3

import socket

hostMACAddress = 'b8:27:eb:2d:17:5a'
#hostMACAddress = 'b8:27:eb:7b:60:24'
port = 3 # 3 is an arbitrary choice. However, it must match the port used by the client.
backlog = 1
size = 4096
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((hostMACAddress,port))
s.listen(backlog)
try:
    client, address = s.accept()
    print('Connected by', address)
    while 1:
        data = client.recv(size)
        if data:
            data_arr = pickle.dumps(data)
            print(data_arr)
            client.send(data_arr)
except:	
    print("Closing socket")	
    client.close()
    s.close()
