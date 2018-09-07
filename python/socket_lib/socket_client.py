# -*- coding: utf-8 -*-
import socket

HOST = ''    # The remote host
PORT = 50007              # The same port as used by the server
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
    print('Received', repr(data))

if __name__ == '__main__':
    main()