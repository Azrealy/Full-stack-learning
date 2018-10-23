# -*- coding: utf-8 -*-
import os
import re
import socket
from concurrent import futures

proxy = os.environ.get("HTTP_PROXY")

if proxy:
    m = re.search(r'^http://(.*)\/$', proxy)
    host = m.group(1).split(":")[0]
    port = int(m.group(1).split(":")[1])

else:
    host = "example.com"
    port = 80

def nonblocking_way():
    sock = socket.socket()
    # setup to sock.connect and sock.recv become no blocking method
    sock.setblocking(False)
    try:
        sock.connect((host, port))
    except BlockingIOError:
        # no blocking sock.connect can also arise Error
        pass
    request = 'GET / HTTP/1.0\r\nHost: example.com\r\n\r\n'
    data = request.encode('ascii')
    # Here we take a while loop to sending data,
    # and the sending will success until the error not arise.
    while True:
        try:
            sock.send(data)
            break
        except OSError:
            pass

    response = b''
    # Same approach like above, take a while loop to receive data,
    # and data will be received completed until error not arise.
    while True:
        try:
            chunk = sock.recv(4096)
            while chunk:
                response += chunk
                chunk = sock.recv(4096)
            break
        except OSError:
            pass

    return response


def sync_way():
    res = []
    for i in range(10):
        res.append(nonblocking_way())
    return len(res)


def main():
    start = time.time()
    print(sync_way())
    print(time.time() - start)


if __name__ == '__main__':
    import time
    main()
