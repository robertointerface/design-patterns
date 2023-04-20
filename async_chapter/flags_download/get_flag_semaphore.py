import asyncio
import time
from typing import List
from httpx import AsyncClient

from pathlib import Path

POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()  # <2>

BASE_URL = 'https://www.fluentpython.com/data/flags'  # <3>
DEST_DIR = Path('../downloaded')                         # <4>


def save_flag(img: bytes, filename: str) -> None:     # <5>
    (DEST_DIR / filename).write_bytes(img)


async def get_flag(client: AsyncClient, cc: str, semaphore) -> bytes:  # <4>
    url = f'{BASE_URL}/{cc}/{cc}.gif'.lower()
    # the client had to be passed from 'supervisor'
    async with semaphore:
        resp = await client.get(url,
                                timeout=6.1,
                                follow_redirects=True)  # <5>
    return resp.read()  # <6>

async def download_one(client: AsyncClient, cc: str, semaphore):  # <3>
    image = await get_flag(client, cc, semaphore)
    # here we are still saving the flat in non async way, later we see how
    # this is done.
    save_flag(image, f'{cc}.gif')
    print(cc, end=' ', flush=True)
    return cc

async def supervisor(cc_list: List[str]):
    # is the same as the code already seen but this time you can set the maximum
    # of concurrent async functions that can happen, change form 0 to 4 in increments
    # of 1 and you can see the difference
    # *******HERE IS WHAT YOU ARE LOOKING FOR**********************
    semaphore = asyncio.Semaphore(4)
    async with AsyncClient() as client:
        to_do = [download_one(client, cc, semaphore)
                 for cc in sorted(cc_list)]
        # gather waits for all to complete.
        res = await asyncio.gather(*to_do)
    return len(res)

def download_many(cc_list: List[str]):
    # all async requests need to be done with asyncio.run() on a root level
    return asyncio.run(supervisor(cc_list))

def main(downloader) -> None:  # <13>
    DEST_DIR.mkdir(exist_ok=True)                          # <14>
    t0 = time.perf_counter()                               # <15>
    count = downloader(POP20_CC)
    elapsed = time.perf_counter() - t0
    print(f'\n{count} downloads in {elapsed:.2f}s')


if __name__ == "__main__":
    main(download_many)
