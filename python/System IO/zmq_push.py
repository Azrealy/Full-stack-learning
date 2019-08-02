import zmq
import time
from random import randint
import concurrent.futures
import argparse

cxt = zmq.Context()
socket = cxt.socket(zmq.PAIR)
socket.bind('tcp://127.0.0.1:5666')

def send_object(id):
    msg = [{"start":id}, {"pending":id}, {"pending":id}, {"complete":id}, {'end':id}]

    for m in msg:
        socket.send_json(m)
        print(f'Push message sucess {m}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", help="increase output verbosity")
    args = parser.parse_args()
    if args.id:
        send_object(args.id)
    else:
        print('You need pass the parameters.')