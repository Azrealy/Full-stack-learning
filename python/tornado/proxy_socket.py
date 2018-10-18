# -*- coding: utf-8 -*-
import socket

request = 'GET http://www.example.org HTTP/1.0\r\nHost: www.example.org\r\n\r\n'

host = "<proxy host>"
port = 8080

s = socket.socket()
s.connect((host, port))
s.send(request.encode('utf-8'))
response = s.recv(3000)
print(response)