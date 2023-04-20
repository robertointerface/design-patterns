
import asyncio
import time
from typing import List
from httpx import AsyncClient
import concurrent.futures
from pathlib import Path

POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()  # <2>
POP20_CC_2 = ('AF AL DZ AS AD AO AI AQ SA SN SC SL SX SK').split()  # <2>

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


async def supervisor(cc_list: List[str]):
    # here the httpx is giving us a context manager and 'client' performs the
    # async http requests, 'requests' library does NOT have async capabilities
    # so do not use the urlib or requests for async programming
    async with AsyncClient() as client:
        to_do = [download_one(client, cc)
                 for cc in sorted(cc_list)]
        # gather waits for all to complete.
        res = await asyncio.gather(*to_do)
    return len(res)

def just_wait():
    time.sleep(3)

async def download_many():
    loop = asyncio.get_running_loop()
    task = loop.create_task(supervisor(POP20_CC))
    # if you comment the line below you would see that the flags are not
    # being downloaded
    count = loop.run_until_complete(task)
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, just_wait)
        print('custom thread pool', result)
    # this is an example of the beauty of asyncio.run(), asyncio.run() closes
    # the loop for you.
    return count


if __name__ == "__main__":
    asyncio.run(download_many())
