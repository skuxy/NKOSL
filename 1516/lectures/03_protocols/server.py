#!/usr/bin/python

import socket,os

s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

try:
    os.remove("/tmp/socketname")
except OSError:
    pass

s.bind("/tmp/socketname")

s.listen(1)

conn, addr = s.accept()

while True:
    data = conn.recv(1024)

    if not data: 
        break
    
    conn.send(data + b" from Server!")

conn.close()

