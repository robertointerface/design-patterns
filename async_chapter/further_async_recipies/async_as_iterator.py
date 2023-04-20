# remember how an iterator is implemented?
# an iterator is an object (remember everything in python is an object)
# that implements methods __iter__ and __next__, so you can build your own custom
# iterator by writting built it methods __next__ and __iter__ on a class
from datetime import datetime
import asyncio
import requests
from httpx import AsyncClient
POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()  # <2>

BASE_URL = 'https://www.fluentpython.com/data/flags'  # <3>
##IMPLEMENTATION OF A CLASSIC ITERATOR, ALL YOU HAVE TO DO IS DEFINE
# methods __iter__ and __next__

class A:

    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        if self.x > 2:
            raise StopIteration
        else:
            self.x += 1
            return self.x

for i in A():
    print(f'i = {i}')


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

class OneFlagAtTheTime:
    """
    we just internally implement __anext__ as in async next, as in an async
    method we can use the await inside
    """
    def __init__(self):
        self.client = AsyncClient()
        self.flags = POP20_CC
        self.flag_counter = 0
    # note here we don't need the async
    def __aiter__(self):
        # iter must return an object that implements __next__ or __anext__
        # that is why we need to return self
        return self

    async def __anext__(self):
        flag = await download_one(self.client, self.flags[self.flag_counter])
        self.flag_counter += 1
        if self.flag_counter >= len(self.flags) - 1:
            raise StopAsyncIteration
        return flag


def normal_flags(flag):
    url = f'{BASE_URL}/{flag}/{flag}.gif'.lower()
    resp = requests.get(url, timeout=6.1)
    return resp.content


async def main():
    # NOTICE THE 'async for' instead of for
    start = datetime.now()
    async for flag in OneFlagAtTheTime():
        print(f'flag {flag}')
    ellapsed = datetime.now() - start
    print(f'ellapsed {ellapsed}')

if __name__ == "__main__":
    # we still need to run async code with asyncio.run()
    asyncio.run(main())

