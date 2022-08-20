#!/bin/bash

import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1])
else:
        print('Invalid input Syntax: python3 PortScannner.py <ip address>')

print('*'*50)
print('port scanning'+target)
print('Scanning time:'+str(datetime.now()))
print('*'*50)

try:
        for port in range(1,1000):
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = s.connect_ex((target,port))
                if result == 0:
                        print('Port {} is open'.format(port))
                        
                s.close()
except KeyboardInterrupt:
        print("\nInterrupted exiting")
        sys.exit()
except socket.gaierror:
        print('host not resloved')
        sys.exit()
except socket.error():
        print('server connection failed')
        sys.exit()

