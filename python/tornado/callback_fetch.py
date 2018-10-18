# -*- coding: utf-8 -*-

import socket
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ

selector = DefaultSelector()
stopped = False
urls_todo = {'/', '/1', '/2', '/3', '/4', '/5', '/6', '/7', '/8', '/9'}

class Crawler:
    def __init__(self, url):
        self.url = url
        self.sock = None
        self.response = b''

    def fetch(self):
        self.sock = socket.socket()
        print(self.sock)
        try:
            host = "<proxy host>"
            port = 8080
            # Set connect to proxy.
            self.sock.connect((host, port))
        except BlockingIOError:
            pass
        fn = self.sock.fileno()
        print(fn)
        print(EVENT_WRITE)
        selector.register(fn, EVENT_WRITE, self.connected)

    def connected(self, key, mask):
        print(key)
        selector.unregister(key.fd)
        get = 'GET http://example.com{0} HTTP/1.0\r\nHost: example.com\r\n\r\n'.format(self.url)
        self.sock.send(get.encode('ascii'))
        selector.register(key.fd, EVENT_READ, self.read_response)

    def read_response(self, key, mask):
        global stopped
        chunk = self.sock.recv(4096)
        if chunk:
            self.response += chunk
        else:
            selector.unregister(key.fd)
            urls_todo.remove(self.url)
            if not urls_todo:
                stopped = True

def loop():
    while not stopped:
        events = selector.select()
        for event_key, event_mask in events:
            print(event_key.data)
            callback = event_key.data
            callback(event_key, event_mask)

if __name__ == '__main__':
    import time
    start = time.time()
    for url in urls_todo:
        crawler = Crawler(url)
        crawler.fetch()
    loop()
    print(time.time() - start)

