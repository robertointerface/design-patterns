"""Basic example of using async for http requests, the classing
download country flags in .gif formats, all the code does is call
http 'https://www.fluentpython.com/data/flags' and ask for the gif of the
country code that we have on POP20_CC."""
import asyncio
import time
from typing import List
from httpx import AsyncClient
from pathlib import Path

POP20_CC = ('CN IN US ID BR PK NG BD RU JP GOKU '
            'MX PH VN ET EG DE IR TR CD FR').split()  # <2>

BASE_URL = 'https://www.fluentpython.com/data/flags'  # <3>
DEST_DIR = Path('../downloaded')                         # <4>


def save_flag(img: bytes, filename: str) -> None:     # <5>
    (DEST_DIR / filename).write_bytes(img)


async def get_flag(client: AsyncClient, cc: str) -> bytes:  # <4>
    url = f'{BASE_URL}/{cc}/{cc}.gif'.lower()
    # the client had to be passed from 'supervisor'
    resp = await client.get(url,
                            timeout=6.1,
                            follow_redirects=True)  # <5>
    return resp.read()  # <6>


async def download_one(client: AsyncClient, cc: str):  # <3>
    image = await get_flag(client, cc)
    # here we are still saving the flat in non async way, later we see how
    # this is done.
    save_flag(image, f'{cc}.gif')
    print(cc, end=' ', flush=True)
    return cc


#IMPORTANT: notice how we put all the async code inside the supervisor,
# this way we know all our async code is inside this function and not
# scatter all around, nice cohesion here
async def supervisor(cc_list: List[str]):
    # here the httpx is giving us a context manager and 'client' performs the
    # async http requests, 'requests' library does NOT have async capabilities
    # so do not use the urlib or requests for async programming
    async with AsyncClient() as client:
        to_do = [download_one(client, cc)
                 for cc in sorted(cc_list)]
        # asyncio.gather waits for all to complete, Note that at this point nothing
        # has started to download, this is because download_one function has
        # 'async' keyword and therefore it needs an await before is executed
        # this brings us to the concept that creating an awaitable object
        # and executing it are 2 different things, an awaitable object will NOT
        # be executed until you call it with an await.
        print(f'STARING TO DOWNLOAD')
        res = await asyncio.gather(*to_do)
        # this code brings us also the importance of asyncio.gather(), if you
        # try to run the code like below, you will see that is slower, that
        # is because they will not be executed simultaniously, they will be done
        # one by one
        """
        for item in to_do:
            await item 
        """
    return len(res)

def download_many(cc_list: List[str]):
    # all async requests need to be done with asyncio.run() on a root level,
    # this way asyncio.run() will take care of the event loop manipulation
    return asyncio.run(supervisor(cc_list))

def main(downloader) -> None:  # <13>
    # This is just timing how long it takes to download all the flags
    DEST_DIR.mkdir(exist_ok=True)                          # <14>
    t0 = time.perf_counter()                               # <15>
    count = downloader(POP20_CC)
    elapsed = time.perf_counter() - t0
    print(f'\n{count} downloads in {elapsed:.2f}s')


if __name__ == "__main__":
    main(download_many)
