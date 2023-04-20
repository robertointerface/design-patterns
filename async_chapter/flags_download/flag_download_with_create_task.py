"""Example on how to run async coroutines with create_task(),
here we are getting dirty and we are creating our own loop, inserting the
tasks into the loop and telling the loop to execute the tasks, NOTICE you
will not see asyncio.run() anywhere."""
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


def download_many(cc_list: List[str]):
    # we create our own loop and set it as active
    loop = asyncio.get_event_loop()
    asyncio.set_event_loop(loop)
    # NOTE that create_task does not start the task, it SCHEDULES it, you
    # still need to run loop.run_until_complete(task)
    task = loop.create_task(supervisor(cc_list))
    # if you comment the line below you would see that the flags are not
    # being downloaded
    count = loop.run_until_complete(task)
    # this is an example of the beauty of asyncio.run(), asyncio.run() closes
    # the loop for you.
    loop.close()
    return count

def main(downloader) -> None:  # <13>
    DEST_DIR.mkdir(exist_ok=True)                          # <14>
    t0 = time.perf_counter()                               # <15>
    count = downloader(POP20_CC)
    elapsed = time.perf_counter() - t0
    print(f'\n{count} downloads in {elapsed:.2f}s')


if __name__ == "__main__":
    main(download_many)
