# -*- coding: utf-8 -*-

import socket
from concurrent import futures


def blocking_way():
    sock = socket.socket()
    # blocking
    host = "<proxy host>"
    port = 8080
    # Set connect to proxy.
    sock.connect((host, port))
    request = 'GET / HTTP/1.0\r\nHost: example.com\r\n\r\n'
    sock.send(request.encode('ascii'))
    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        # blocking
        chunk = sock.recv(4096)
    return response


def thread_way():
    workers = 10
    with futures.ThreadPoolExecutor(workers) as executor:
        thread_futures = {executor.submit(blocking_way) for i in range(10)}
    return len([future.result() for future in thread_futures])


def sync_way():
    res = []
    for i in range(10):
        res.append(blocking_way())
    return len(res)


def main():
    start = time.time()
    print(sync_way())
    print(time.time() - start)


if __name__ == '__main__':
    import time
    main()