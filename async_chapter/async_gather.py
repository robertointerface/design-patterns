"""Why use gather? why not just call the awaits one after another?,
we see in the following example"""
import asyncio
import datetime


async def infinite_print(function_ref: int):
    while True:
        print(f"{function_ref}: {datetime.datetime.now()}")
        await asyncio.sleep(2)


async def run_no_gather():
    # here we are stock on the first awaitable
    await infinite_print(1)
    await infinite_print(2)
    await infinite_print(3)


async def run_gather():
    # here we execute all at the same time
    await asyncio.gather(infinite_print(1),
                         infinite_print(2),
                         infinite_print(3))


asyncio.run(run_no_gather())
