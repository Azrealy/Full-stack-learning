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