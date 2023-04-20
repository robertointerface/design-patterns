import asyncio

async def doubler(a):
    for i in range(a):
        await asyncio.sleep(1)
        yield i * 2

async def main():
    double_values = [i async for i in doubler(4)]
    print(f'double_values {double_values}')

async def await_function():
    await asyncio.sleep(1)
    print(f'after await')

async def await_list():
    await asyncio.sleep(3)
    await_list = [await_function, await_function, await_function]
    for i in await_list:
        yield i

async def main_2():
    [await i() async for i in await_list()]

asyncio.run(main_2())

