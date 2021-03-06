import asyncio
import zmq.asyncio
from tornado.ioloop import IOLoop


queue = asyncio.Queue()
ctx = zmq.asyncio.Context()

async def pushing():
    server = ctx.socket(zmq.PUSH)
    server.bind('tcp://127.0.0.1:9000')
    while True:
        await server.send(b"Hello")
        await asyncio.sleep(1)

async def pulling():
    client = ctx.socket(zmq.PULL)
    client.connect('tcp://127.0.0.1:9000')
    while True:
        greeting = await client.recv()
        print(greeting)

def zmq_tornado_loop():
    loop = IOLoop.current()
    loop.spawn_callback(pushing)
    loop.spawn_callback(pulling)
    loop.start()

if __name__ == "__main__":
    zmq_tornado_loop()
