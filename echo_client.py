#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A simple TCP echo client

"""

import os, sys
import socket
import time
import string, random
import threading

# Set up socket, get IP, port and how many packets to send from commandline
try:
    host = sys.argv[1] 
    port = int(sys.argv[2]) 
    num_pkts = int(sys.argv[3])
except IndexError:
    file_ = sys.argv[0]
    sys.stderr.write('Usage: ' + '%s SERVER-IP PORT PACKETS \n' %(file_))
    sys.exit(1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True) #Disable Nagle's
s.connect((host, port))

FORMAT = 'utf-8'
SZ = 1420
count = 0
pkt_nr = 1


def padding(msg):
    padding = bytes(chr(random.randint(1,31)), encoding=FORMAT)
    
    extra = 1400 - len(msg)
    if extra > 0:
        msg += padding * extra
    return msg

def unpadding(msg):
    
    last_char = msg[-1]
    if last_char.isdigit() == False:
        return msg.rstrip(last_char)
    else:
        return msg
    

def _send(msg):
    s.sendall(msg)
    

print('pkt_nr ts rtt size')
while count < num_pkts:
    time_sent = time.time() 
    text = str(time_sent).encode(FORMAT)
    txt_to_send = padding(text)
    
    thread_send = threading.Thread(target=_send, args=(txt_to_send,))
    thread_send.start()
    
    
    data = s.recv(1420)
       
    data = data.decode(FORMAT)
    unpadded = unpadding(data)

    elapsed_time = time.time()
    time_diff = (elapsed_time-float(unpadded))*1000
    time_conv = '{:.3f}'.format(time_diff)
    print('{} {} {} {}'.format(pkt_nr, repr(unpadded), time_conv, len(data)))
    
    pkt_nr+=1
    count+=1
    
s.close()