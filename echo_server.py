#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created by Emilia Weyulu on Sun Aug 01 23:47:18 2020
Copyright (c) 2020 Emilia Weyulu <eweyulu@mpi-inf.mpg.de>.

"""

# echo_server.py
import os, sys
import socket

host = ''   # The socket is reachable by any address the machine happens to have

try:
    port = int(sys.argv[1]) 
except IndexError:
    file_ = sys.argv[0]
    sys.stderr.write('Usage: ' + '%s PORT \n' %(file_))
    sys.exit(1)

DISCONNECT_MESSAGE = "!DISCONNECT" 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)

connected = True
while connected:
    data = conn.recv(1420)
    if not data: 
        break
    conn.sendall(data)
    
#conn.close()