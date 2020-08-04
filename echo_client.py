#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created by Emilia Weyulu on Sun Aug 01 23:47:18 2020
Copyright (c) 2020 Emilia Weyulu <eweyulu@mpi-inf.mpg.de>.

"""

# echo_client.py
import os, sys
import socket
import time
import string, random

# Set up socket, get IP, port and how many packets to send from commandline
host = sys.argv[1] 
port = int(sys.argv[2]) 
num_pkts = int(sys.argv[3])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

FORMAT = 'utf-8'
count = 0
pkt_nr = 1


def padding(msg):
    padding = bytes(chr(random.randint(1,31)), encoding=FORMAT)
    
    extra = 1420 - len(msg)
    if extra > 0:
        msg += padding * extra
    return msg

def unpadding(msg):
    
    last_char = msg[-1]
    if last_char.isdigit() == False:
        return msg.rstrip(last_char)
    else:
        return msg

print('pkt_nr size rtt')
while count < num_pkts:
    time_sent = time.time() 
    text = str(time_sent).encode(FORMAT)
    to_send = padding(text)
    
    s.sendall(to_send)

    data = s.recv(1420)
    data = data.decode(FORMAT)
    unpadded = unpadding(data)

    time_recv = time.time()
    time_diff = (time_recv-time_sent)*1000
    time_conv = '{:.3f}'.format(time_diff)
    print('{} {} {} {}'.format(pkt_nr, repr(unpadded), time_conv, len(data)))
    
    pkt_nr+=1
    count+=1
    
s.close()
