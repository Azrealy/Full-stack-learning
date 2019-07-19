import zmq.asyncio
import random
import sys
import time
import asyncio
from tornado.ioloop import IOLoop

msg = [{"alice":1}, {"josh":1}, {"rose":1}, {"fowww":1}, {'end':1}]

async def pair_client():
    context = zmq.asyncio.Context()
    socket = context.socket(zmq.PAIR)
    socket.connect("ipc:///tmp/socket")
    for m in msg:
        await socket.send_json(m)
        time.sleep(1)
    socket.close()
    context.term()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(pair_client())