from random import randint
import zmq.asyncio
import random
import sys
import time
import asyncio
import tornado
from tornado.process import Subprocess
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def initialize(self, socket):
        self.socket = socket
    async def post(self):
        id = self.get_body_argument('id', None)
        def callback(msg):
            self.write(msg)
            self.write('\r\n')
            self.flush()
        if id: 
            result = await start_exec(id, self.socket, callback)
            self.write(str(result))
            self.write('\r\n')
            self.finish()


class Message:
    def __init__(self, id, state):
        self.id = id
        self.state = state
    
    def update(self, state):
        print(f"Message {self.id} state updated from {self.state} to {state}")
        self.state = state
        
    def __repr__(self):
        return repr(f"Message id: {self.id} state: {self.state}")

def pair_client():
    context = zmq.asyncio.Context()
    socket = context.socket(zmq.PAIR)
    socket.connect("tcp://127.0.0.1:5666")
    app = tornado.web.Application([
        (r"/", MainHandler, dict(socket=socket)),
    ])
    app.listen(8888)
    print("Server start at 8888")

async def start_exec(id, socket, callback):
    Subprocess(['python', 'zmq_push.py', '--id', str(id)])
    result = Message(id, None)
    while True:
        msg = await socket.recv_json()
        print('received message %s' % msg)
        if "start" in msg:
            result.update('start')
        elif "pending" in msg:
            result.update('pending')
        elif "complete" in msg:
            result.update('complete')
        elif "end" in msg:
            result.update('end')
            break
        callback(msg)
    print(f"Message {result} received completed.")
    return result

if __name__ == "__main__":
    io_loop = tornado.ioloop.IOLoop.current()
    pair_client()
    io_loop.start()