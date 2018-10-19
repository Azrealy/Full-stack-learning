# socket a lib of networking interface

### Basic sockets.method

* `socket objects` will be call like `socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, filno=None)`.

* `socket.connect(address)` Connect to a remote socket at address. When the connect completes, the socket s can be used to send in a request for the text of the page. (The format of address depends on the address family). what means if you set `family=AF_INET` to the `socket.socket` then the address here wil be a pair `(host, post)`.

* `socket.recv(bufsiz[, flags])` Receive data from socket. The return value is a bytes object representing the data received.

* `socket.send(bytes[, flags])` should be used after be connected to remote socket. Also usable to send request bytes to the server. Returns the number of bytes sent.

* `socket.listen([backlog])` Enable a server to accept connections. If backlog is specified, it must be at least 0, it specifies the number of unaccepted connections that the system will allow before refusing new connections.

* `socket.bind(address)` Bind the socket to address.

* `socket.accept()` Accept a connection. The socket must be bound to an address and listening for connections. The return value is a pair `(conn, address)` where **conn** is a new socket object usable to `conn.send()` and `conn.recv`
data the connection, address is bound to the socket on the other end of the connection.

# Socket as Client.

The step of programming a socket as client:
1. Create a socket using `sock = socket.socket()`.
  * Address Family: AF_INET this mean IP version is IPv4
  * Type: SOCK_STREAM this mean connection use TCP protocol.
2. Connect tp remote server using `sock.connect((host, port))`
3. Send data using `sock.send("GET / HTTP/1.1\r\n\r\n")`. (Usually we call this data as request, which always include Method, Protocol Type, Url and Header).
4. Receive a reply using `sock.rev(4096)`, (Enable to receive a specify buffer size of data.)
5. Close the socket. `sock.close()`.

# Socket as Servers

Onto server things, Server socket programming also like following:
1. Open a socket using `sock = socket.socket()`
2. Bind to a address and port `sock.bind((host, port))`.
    * host = '' means symbolic name meaning all available interfaces
    * port = 8101 use arbitrary non-privileged port.
3. Listen for incoming connections using `sock.listen(10)`.
    * The parameter of the `socket_listen` function listen is called backlog. It controls the number of incoming connections that are kept waiting if the program is already busy. Here by specifying 10, it means that if 10 connections have already been waiting to be processed, then 11th connection request shall be rejected.
4. Accept connections using `conn, addr = sock.accept()`.
    * This is a blocking call means to waiting to accept a connection.

5. Read and Send `conn.recv(1034)` and `conn.sendall(data)`.
    * We can pu the `socket_accept` in a while loop for keeping server running nonstop.

# Handling Connections

As we can use while loop to make our socket server nonstop running like following,
```python
import socket
import sys
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 5000 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
 
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
     
print('Socket bind complete')
 
s.listen(10)
print('Socket now listening')
 
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
     
    data = conn.recv(1024)
    reply = b'OK...' + data
    if not data: 
        break
     
    conn.sendall(reply)
 
conn.close()
s.close()
```
but also it si not able to handle more than i connection at a time. Here is using thread to handle multiple connections.
```python
import socket
import sys
import _thread
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8889 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
     
print('Socket bind complete')
 
#Start listening on socket
s.listen(10)
print('Socket now listening')
 
#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    conn.send(b'Welcome to the server. Type something and hit enter\n') #send only takes string
     
    #infinite loop so that function do not terminate and thread do not end.
    while True:
         
        #Receiving from client
        data = conn.recv(1024)
        reply = b'OK...' + data
        if not data: 
            break
     
        conn.sendall(reply)
     
    #came out of loop
    conn.close()
 
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    _thread.start_new_thread(clientthread ,(conn,))
 
s.close()
```
The above connection handler takes some input from the client and replies back with the same.