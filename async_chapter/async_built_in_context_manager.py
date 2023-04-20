
import asyncio
import httpx
from contextlib import asynccontextmanager
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

# this is the same as flag download async context but with the already handy
# built in asynccontextmanager
@asynccontextmanager
async def get_flags():
    async with AsyncClient() as client:
        to_do = [download_one(client, flag) for flag in POP20_CC]
        yield await asyncio.gather(*to_do)
        print(f'############CLEARING HERE###############')


async def download_flags():
    async with get_flags() as flags:
        print(f'flags {flags}')


asyncio.run(download_flags())
