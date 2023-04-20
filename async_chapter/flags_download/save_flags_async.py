"""
This code is the same as before, we are requesting flags and we are
saving them, in the previous examples the function saving_flags was NOT async
and was blocking our async code, we did not see much difference on the time
because it was saving a few bytes and that is fast, but in this example I have
introduced a delay on purpose on the function save_flag_with_delay to highlight
how non async code can block your code and stop you from getting all the async
benefits.

To solve this problem asyncio has introduced a methodology for you to execute
code that is impossible to execute in an async way on your async code, that way
you can still get the best of async.
"""
import asyncio
import time
from typing import List
from httpx import AsyncClient
from concurrent import futures
from pathlib import Path


POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()  # <2>

BASE_URL = 'https://www.fluentpython.com/data/flags'  # <3>
DEST_DIR = Path('../downloaded')                         # <4>

prime_list_result = []
def save_flag(img: bytes, filename: str) -> None:     # <5>
    (DEST_DIR / filename).write_bytes(img)

def save_flag_with_delay(img: bytes, filename: str):
    time.sleep(2)
    (DEST_DIR / filename).write_bytes(img)


async def get_flag(client: AsyncClient, cc: str) -> bytes:  # <4>
    url = f'{BASE_URL}/{cc}/{cc}.gif'.lower()
    # the client had to be passed from 'supervisor'
    resp = await client.get(url,
                            timeout=6.1,
                            follow_redirects=True)  # <5>
    return resp.read()  # <6>

"""HERE IS WHERE YOU HAVE TO PAY ATTENTION.

"""
FUTURES = []
async def download_one(client: AsyncClient, cc: str):  # <3>
    image = await get_flag(client, cc)
    # here we save the flag on a different thread by using the run_in_executor
    loop = asyncio.get_running_loop()
    """
    if we uncomment the line below and we comment the ProcessPoolExecutor
    we will see how we are blocking everything
    """
    # save_flag_with_delay(image, f'{cc}.gif')
    """
    The code below shows how you can run blocking function on asyncio, the 
    function save_flag_with_delay will block the event loop as the code inside
    uses time.sleep(2) which is not async and stops the main thread there, in
    order to overcome this problem which can happen for example when using 
    aws botocore library what you can do is use the method run_in_executor, this
    method will take your blocking function and first run it on a different thread
    or process BUT will also convert that thread/process function into an asyncio
    'future' that is why you can use the word 'await', remember that when you 
    use threads or processes you have to use the 'futures' library, that is because
    thread/process 'futures' are similar to asyncio 'futures', futures are objects
    that encapsulate pending operations that we can put on queues and then check
    when they are done and we can retrieve their results. 
    """
    with futures.ThreadPoolExecutor() as executor:
        # NOTICE THAT WE CAN USE THE WORD AWAIT, THAT IS BECAUSE run_in_executor
        # TAKES A THREAD/PROCESS FUTURE AND CONVERTS IT INTO ASYNCIO FUTURE.
        await loop.run_in_executor(executor,
                                   save_flag_with_delay,
                                   image, f'{cc}.gif')
    print(cc, end=' ', flush=True)
    return cc

# the code below is the same as other examples
async def supervisor(cc_list: List[str]):
    async with AsyncClient() as client:
        to_do = [download_one(client, cc)
                 for cc in sorted(cc_list)]
        # gather waits for all to complete.
        res = await asyncio.gather(*to_do)
        # to_do_list = asyncio.as_completed(to_do)
        # for coro in to_do_list:
        #     status = await coro
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
