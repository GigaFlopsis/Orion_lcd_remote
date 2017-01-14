#!/usr/bin/env python

# autor - Devitt Dmitry\
# date 14.01.2017

import socket
import sys


TCP_IP = '192.168.1.1'
TCP_PORT = 9761
BUFFER_SIZE = 1024
msg_ON = bytes.fromhex('0240010003')
msg_OFF = bytes.fromhex('0241010003')

def send_cmd(cmd):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    if cmd == 'ON':
        s.send(msg_ON)
    if cmd == 'OFF':
        s.send(msg_OFF)
    data = s.recv(BUFFER_SIZE)
    s.close()
    # print("received data:", data)



if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd = str(sys.argv[1])
        if (cmd != 'ON' or cmd != 'ON'):
             print('ERROR! Sin ON and OFF')
        else:
            send_cmd(cmd)
    else:
       while True:
        cmd = str(input('sin ON and OFF: '))
        if (cmd != 'ON' or cmd != 'ON'):
             print('ERROR! Sin ON and OFF')
             continue
        else:
            send_cmd(cmd)


