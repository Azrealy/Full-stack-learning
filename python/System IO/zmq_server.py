import time
import zmq

def pair_server():
	context = zmq.Context()
	socket = context.socket(zmq.PAIR)
	socket.bind("ipc:///tmp/socket")
	while True:
		msg = socket.recv_json()
		print(msg)
		if "end" in msg:
			break
	socket.close()
	context.term()

if __name__ == "__main__":
    pair_server()