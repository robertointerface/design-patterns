import asyncio
from asyncio import StreamReader, StreamWriter


async def echo(reader: StreamReader, writer: StreamWriter):
    print(f'new connections')
    try:
        while data := await reader.readline():
            upper_data = str(data).upper()
            writer.write(str.encode(upper_data))
            await writer.drain()
        print(f'Leaving connection')
    except asyncio.CancelledError:
        print('Connection dropped!')

async def main(host='127.0.0.1', port=8888):
    server = await asyncio.start_server(echo, host, port)
    async with server:
        await server.serve_forever()

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print('Bye!')
