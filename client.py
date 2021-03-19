#!/usr/bin/env python3

import socket, time
from _thread import *

host_start = 2
host_end = 19
host_except = [5]
PORT = 65432        # The port used by the server
expected_size = 200000
done = 0
def multi_threaded_client(host,port):
    global done
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(host)
        s.connect((host,port))
        for i in range(20):
            s.sendall(b'Hello, world')
            sum = 0
            while(sum < expected_size):
                data = s.recv(1024)
                sum+=len(data)
        done += 1
start = time.time()
for i in range(host_start,host_end+1):
    if(i in host_except):
        continue
    host = '192.168.2.' + str(i)
    print(host)
    start_new_thread(multi_threaded_client,(host,PORT))
while(done != host_end-host_start+1 - len(host_except)):
    continue
end = time.time()
print(end-start)
