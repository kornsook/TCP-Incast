#!/usr/bin/env python3

import socket, time
from _thread import *

host_start = 2
host_end = 22
host_except = [5]
PORT = 65432        # The port used by the server
expected_size = 200000
n_packets = 5
done = 0
def multi_threaded_client(host,port):
    global done
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host,port))
        s.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,True)
        s.sendall(b'Hello, world')
        sum = 0
        while(sum < expected_size):
            data = s.recv(1024)
            sum+=len(data)
        done += 1
for i in range(host_start,host_end+1):
    if(i in host_except):
        continue
    num_except = 0    
    for j in host_except:
        if(j <= i):
            num_except += 1
    N = i - host_start + 1 - num_except
    print('N = {}'.format(N))
    start = time.time()
    for k in range(n_packets):
        done = 0
        for j in range(host_start,i+1):
            if(j in host_except):
                continue
            host = '192.168.2.' + str(j)
            start_new_thread(multi_threaded_client,(host,PORT))
        while(done != N):
            continue
    end = time.time()
    print('Latency: {} sec\nGoodput: {} Mbps'.format(end-start, expected_size*n_packets*8*(10**(-6))*N/(end-start)))
