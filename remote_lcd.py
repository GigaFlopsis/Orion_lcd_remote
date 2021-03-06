#!/usr/bin/env python

# autor - Devitt Dmitry\
# date 14.01.2017

import socket
import sys

TCP_IP = '192.168.1.1'
TCP_PORT = 9761
BUFFER_SIZE = 1024

msg_ON = b'\x02@\x01\x00\x03'

msg_OFF = b'\x02A\x01\x00\x03'

def send_cmd(cmd):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    if cmd == '1':
        print('On lcd')
        s.send(msg_ON)
    if cmd == '0':
        print('OFF lcd')
        s.send(msg_OFF)
    data = s.recv(BUFFER_SIZE)
    s.close()
    # print("received data:", data)



if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd = str(sys.argv[1])
        if (cmd != '1' and cmd != '0'):
             print('ERROR! Sin 1 (ON) and 0 (OFF)')
        else:
            send_cmd(cmd)
    else:
       while True:
        cmd = str(input('Sin 1 (ON) and 0 (OFF)'))
        if (cmd != '1' and cmd != '0'):
             print('ERROR! Sin ON and OFF')
             continue
        else:
            send_cmd(cmd)

