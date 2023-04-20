"""
you can use asyncio to create async generators, remember generators use the
keyword 'yield'. Below you can fine

"""
from datetime import datetime
import requests
import asyncio
from httpx import AsyncClient
POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()  # <2>

BASE_URL = 'https://www.fluentpython.com/data/flags'  # <3>


"""*****************ASYNC WAY**********************"""
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

async def flags():
    async with AsyncClient() as client:
        for flag in POP20_CC:
            value = await download_one(client, flag)
            yield value
"""***********************************************"""

"""************** NORMAL (NON-ASYNC WAY)*******************"""
def normal_flags(flag):
    url = f'{BASE_URL}/{flag}/{flag}.gif'.lower()
    resp = requests.get(url, timeout=6.1)
    return resp.content


def normal_flags_generator():
    for flag in POP20_CC:
        value = normal_flags(flag)
        yield value

def non_async_main():
    start = datetime.now()
    for flag_data in normal_flags_generator():
        print(flag_data)
    ellapsed = datetime.now() - start
    print(f'ellapsed {ellapsed}')

"""*******************************************************"""


async def main():
    start = datetime.now()
    """the same way you iterate of a generator but this time you need to 
    put async infront of for loop consumption."""
    async for flag_data in flags():
        print(flag_data)
    ellapsed = datetime.now() - start
    print(f'ellapsed {ellapsed}')


# comment to use async and non-async way
asyncio.run(main())
#non_async_main()
