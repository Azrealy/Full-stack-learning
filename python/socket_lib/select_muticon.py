# -*- coding: utf-8 -*-
import socket
import selectors
import types

select = selectors.DefaultSelector()
sock = socket.socket()

host = "localhost"
port = 8990

sock.bind((host, port))
sock.listen(10)
print("listening on", (host, port))
# Config this socket in non-blocking mode.
sock.setblocking(False)
# Registers the socket to be monitored readable event use select.
# use data to keep track of what's been sent and received on the socket.
select.register(sock, selectors.EVENT_READ, data=None)

def event_loop():
    while True:
        # track the sockets if it ready for I/O
        events = select.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                # client socket that's already been accepted.
                handle_accept(key.fileobj)
            else:
                handle_connection(key, mask)

def handle_accept(sock):
    connect, address = sock.accept()
    print('Socket emit a readable event and accepted connection from', address)
    connect.setblocking(False)
    data = types.SimpleNamespace(address=address, input=b'', output=b'')
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    # Register a client connetion is ready for reading and writing with the data.
    select.register(connect, events, data=data)

def handle_connection(key, mask):
    sock = key.fileobj
    data = key.data
    print(mask)
    if mask and selectors.EVENT_READ:
        recv_data = sock.recv(1024) # should ready to read
        if recv_data:
            data.output += recv_data
        else:
            print('closing connection to as recv_data is None', data.addr)
            select.unregister(sock)
    if mask and selectors.EVENT_WRITE:
        if data.output:
            print('echoing', repr(data.output), 'to', data.address)
            sent = sock.send(data.output)
            data.output = data.output[sent:]

if __name__ == '__main__':
    event_loop()
