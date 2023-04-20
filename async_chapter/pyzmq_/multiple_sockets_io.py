import asyncio
import time

import zmq
from zmq.asyncio import Context

context = Context()

async def do_receiver():
    receiver = context.socket(zmq.PULL)
    receiver.connect("tcp://localhost:5557")
    while message := await receiver.recv_json():
        print(f'Via PUll: {message}')
        await asyncio.sleep(3)

async def do_subscriber():
    subscriber = context.socket(zmq.SUB)
    subscriber.connect("tcp://localhost:5556")
    subscriber.setsockopt_string(zmq.SUBSCRIBE, '')
    while message := await subscriber.recv_json():
        print(f'Via sub: {message}')
        await asyncio.sleep(3)
async def main():
    await asyncio.gather(do_receiver(), do_subscriber())

asyncio.run(main())
