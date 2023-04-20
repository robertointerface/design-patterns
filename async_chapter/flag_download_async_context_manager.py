import asyncio
from httpx import AsyncClient
POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()  # <2>

BASE_URL = 'https://www.fluentpython.com/data/flags'  # <3>

async def get_flag(client: AsyncClient, cc: str) -> bytes:  # <4>
    url = f'{BASE_URL}/{cc}/{cc}.gif'.lower()
    resp = await client.get(url,
                            timeout=6.1,
                            follow_redirects=True)  # <5>
    return resp.read()  # <6>

async def download_one(client: AsyncClient, cc: str):  # <3>
    image = await get_flag(client, cc)
    print(cc, end=' ', flush=True)
    return image

class FlagsData:

    def __init__(self):
        self.images = []

    async def __aenter__(self):
        async with AsyncClient() as client:
            to_do = [download_one(client, flag) for flag in POP20_CC]
            self.images = await asyncio.gather(*to_do)
        return self.images

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f'####################exiting##################')
        self.images = []


async def download_flags():
    async with FlagsData() as flags:
        # flags is an iterable as is what is returned from __aenter__
        for flag in flags:
            print(f'flags {flag}')
    print(f'outside context manager')


asyncio.run(download_flags())
