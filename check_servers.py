#!/usr/bin/env python3

import socket, time

host_start = 2
host_end = 22
ClientSocket = socket.socket()
port = 65432

print('List of servers that have problems:')
for i in range(host_start, host_end+1):
    host = '192.168.2.' + str(i)
    try:
        ClientSocket.connect((host, port))
    except socket.error as e:
        print(host)