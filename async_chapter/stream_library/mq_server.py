import asyncio
from collections import deque, defaultdict
from typing import Deque, DefaultDict
from asyncio import StreamReader, StreamWriter, gather

SUBSCRIBERS: DefaultDict[bytes, Deque] = defaultdict(deque)


async def client(reader: StreamReader, writer: StreamWriter):
    peername = writer.get_extra_info('peername')
    subscriber_chan = await read_msg(reader)
    SUBSCRIBERS[subscriber_chan].append(writer)
    print(f"remote {peername} subscribed to {subscriber_chan}")
    try:
        while channel_name := await read_msg(reader):
            data = await read_msg(reader)
            print(f"sending to {channel_name}: {data[:19]}")
            conns = SUBSCRIBERS[channel_name]
            if conns and channel_name.startswith(b'/queue'):
                conns.rotate()
                conns = [conns[0]]
            await gather(*[send_msg(c, data) for c in conns])
    except asyncio.CancelledError:
        print(f"Remote {peername} closing connection")
        writer.close()
        await writer.wait_closed()
    except asyncio.IncompleteReadError:
        print(f"remote {peername} disconnected")
    finally:
        print(f"Remote {peername} closed")
        SUBSCRIBERS[subscriber_chan].remove(writer)

async def main(*args, **kwargs):
    server = await asyncio.start_server(*args, **kwargs)
    async with server:
        await server.serve_forever()

try:
    asyncio.run(main(client, host='127.0.0.1', port=25000))
except KeyboardInterrupt:
    print('Bye!')
