"""Let's say you want to create a function that needs to get some data about
the capture first.
Then perform some computation and after that computation is finished you need
to make a http call to update some statistics about that specific capture."""
import httpx
from contextlib import asynccontextmanager



@asynccontextmanager
async def web_page(capture_id: str):
    url = f'darkroom_url/{capture_id}'
    async with httpx.AsyncClient() as client:
        data = await client.get(url, timeout=3.1, follow_redirects=True)
        # everything executed until the yield is what is executed normally
        # in the __enter__ method of the traditional way of doing context
        # manager
        yield data
        # everything after the yield is executed normally on the __exit__
        # method of the traditional way of doing context manager
        update_data = {'updating': 'updating'}
        await client.post(url, data=update_data, timeout=3)

# the example below is the same as above but we are taking care of possible
# errors by catching them
@asynccontextmanager
async def web_page_with_failure_handling(capture_id: str):
    url = f'darkroom_url/{capture_id}'
    async with httpx.AsyncClient() as client:
        try:
            data = await client.get(url, timeout=3.1, follow_redirects=True)
            yield data
        except httpx._exceptions.HTTPError:
            msg = f'Could not get data from capture {capture_id}'
            raise ValueError(msg)
        update_data = {'updating': 'updating'}
        await client.post(url, data=update_data, timeout=3)


def something_amazing_with_capture_data(capture_data):
    pass


"""************************START HERE****************"""
"""this function uses the async context manager created above """
def super_amazing_function_by_juil(capture_id):
    # NOTICE THE async INFRONT OF THE WITH
    async with web_page(capture_id) as capture_data:
        # the capture_data is what is yielded from the context manager.
        something_amazing_with_capture_data(capture_data)



