#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created by Emilia Weyulu on Sun Aug 01 23:47:18 2020
Copyright (c) 2020 Emilia Weyulu <eweyulu@mpi-inf.mpg.de>.

"""

# echo_server.py
import os, sys
import socket

host = ''        # Symbolic name meaning all available interfaces
port = int(sys.argv[1]) 

DISCONNECT_MESSAGE = "!DISCONNECT" 

#port = 12345     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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