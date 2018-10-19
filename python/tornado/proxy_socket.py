# -*- coding: utf-8 -*-
import socket
import os
import re

proxy = os.environ.get("HTTP_PROXY")

if proxy:
    m = re.search(r'^http://(.*)\/$', proxy)
    host = m.group(1).split(":")[0]
    port = int(m.group(1).split(":")[1])

else:
    host = "example.org"
    port = 80

print("Set connection to {} host and {} port".format(host, port))

request = 'GET http://www.example.org HTTP/1.0\r\nHost: www.example.org\r\n\r\n'

s = socket.socket()
s.connect((host, port))
s.send(request.encode('utf-8'))
response = s.recv(3000)
print(response)