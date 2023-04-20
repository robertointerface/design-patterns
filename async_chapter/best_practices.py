import asyncio
"""
1 - create an async main function that is the entrance to all your async code
"""

async def _sleep():
    await asyncio.sleep(0.5)

async def _print_and_sleep():
    print(f'sleeping')
    await asyncio.sleep(0.5)

"""This way we can debug easier as we know that all the async code is inside
this main_async method"""
async def main_async():
    await_functions = [_sleep(), _print_and_sleep()]
    await asyncio.gather(*await_functions)


asyncio.run(main_async())


