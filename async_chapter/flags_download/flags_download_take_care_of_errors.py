"""
This is the classical download flag code BUT in this case we are introducing
a non-existing country to raise an error on purpose as when we try to get
the flag for that country http request will raise an error.

This is an example on how to handle errors with concurrent tasks
running, what happens when you are trying to download multiple contents at the
same time and for example ONLY one fails?

1 - the first case is that you stop all executions immediately and find which
specific case failed, in this case the pending tasks will be stopped and not
executed, this example is on function download_many_stop_execution_if_raised_error

2 - the second case is when you do not raise an error and let all the still
pending tasks to be finished, then be notified of what specific tasks failed, this
is shown when you use function download_many_let_all_the_tasks_finished
"""
import asyncio
from typing import List
from httpx import AsyncClient
from httpx._status_codes import codes
from pathlib import Path

# DRAGON_BALL IS NOT A COUNTRY CODE, UNFORTUNATEL.
POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR DRAGON_BALL CD FR AG AZ BS BH BD BF BI KH CM CA '
            'DM SV ER EE MC DK HT ZM NP NI MR MU').split()  # <2>
BASE_URL = 'https://www.fluentpython.com/data/flags'  # <3>
DEST_DIR = Path('../downloaded')                         # <4>

def save_flag(img: bytes, filename: str) -> None:     # <5>
    if not DEST_DIR.exists():
        DEST_DIR.mkdir()
    (DEST_DIR / filename).write_bytes(img)


async def get_flag(client: AsyncClient, cc: str) -> bytes:  # <4>
    url = f'{BASE_URL}/{cc}/{cc}.gif'.lower()
    # the client had to be passed from 'supervisor'
    resp = await client.get(url,
                            timeout=5,
                            follow_redirects=True)  # <5>
    if not codes.is_success(resp.status_code):
        raise asyncio.CancelledError(f'Could not get flag {cc}')
    return resp.read()  # <6>

async def download_one(client: AsyncClient, cc: str):  # <3>
    image = await get_flag(client, cc)
    # here we are still saving the flat in non async way, later we see how
    # this is done.
    save_flag(image, f'{cc}.gif')
    print(cc, end=' ', flush=True)
    return cc



async def download_many_let_all_the_tasks_finished(cc_list: List[str]) -> None:
    client = AsyncClient()
    to_do = [download_one(client, cc)
             for cc in sorted(cc_list)]
    """Extremely important topic here is the return_exceptions, 
    the default is False which means that when an error is encountered
    it is raised (unless is handled) but when return_exceptions is True
    that means that errors will not be raised but will be returned as a 
    result so user can inspect them"""
    """
    if use the line below then an exception is raised an we execute
    the except block below"""
    # await asyncio.gather(*tasks, return_exceptions=False)
    """
    If on the other hand we execute the code as below line then
    the exception is not raised and instead the exception is returned
    as result for our investigation, the key fact is that when
    the exception is not raised it allows us to run all the tasks
    """
    results = await asyncio.gather(*to_do, return_exceptions=True)
    print(f'results {results}')


async def download_many_stop_execution_if_raised_error(cc_list: List[str]):
    async with AsyncClient() as client:
        to_do = [download_one(client, cc)
                 for cc in sorted(cc_list)]
        # gather waits for all to complete.
        try:
            res = await asyncio.gather(*to_do)
            print(f'\n results {res}')
        except asyncio.CancelledError:
            # errors are caught here.
            print(f'HANDLING CancelledError')
            loop = asyncio.get_running_loop()
            # if any error we can get the tasks on the running loop, the running
            # loop removes tasks as they finished so at this point there is only pending
            # tasks when you call all_tasks
            pending_tasks = asyncio.all_tasks(loop)
            pending_flags = []
            # iterate over each pending task and just get the task argument on a
            # nasty way
            for task in pending_tasks:
                coro = task.get_coro()
                pending_flags.append(coro.cr_frame.f_locals.get('cc'))
            print(f'\n pending flags that could not be obtained {pending_flags}')
            return
    return len(res)


if __name__ == "__main__":
    asyncio.run(download_many_stop_execution_if_raised_error(POP20_CC))

