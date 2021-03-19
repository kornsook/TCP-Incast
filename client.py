#!/usr/bin/env python3

import socket, time
from _thread import *

HOST_LIST = ['192.168.2.2']  # The server's hostname or IP address
PORT = 65432        # The port used by the server
expected_size = 200000
done = 0
def multi_threaded_client(host,port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host,PORT))
        for i in range(20):
            s.sendall(b'Hello, world')
            sum = 0
            while(sum < expected_size):
                data = s.recv(1024)
                sum+=len(data)
        done += 1
        connection.close()
start = time.time()
for host in HOST_LIST:    
    multi_threaded_client(host,port)
while(done != len(HOST_LIST)):
    continue
end = time.time()
print(end-start)
