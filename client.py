#!/usr/bin/env python3

import socket, time

HOST = '192.168.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    start = time.time()
    for i in range(20):
        s.sendall(b'Hello, world')
        sum = 0
        for i in range(1000):
            data = s.recv(1024)
            sum+=len(data)
    end = time.time()
    print(end-start)
