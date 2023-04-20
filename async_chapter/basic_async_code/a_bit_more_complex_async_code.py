import asyncio

"""
WHAT TO LOOK FOR:
- you can manipulate the event loop directly.
- function run_until_complete()
"""

# async functions need to start with 'async'
async def main():
    # we need to use 'await' to stop executing code inside the 'async' block
    # until we get a response and execute other async functions in the meantime
    # while we wait for a response.
    print('waiting')
    await asyncio.sleep(3)


if __name__ == "__main__":
    # if you use just asyncio.run(), all the below is done for you
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    task = loop.create_task(main())
    loop.run_until_complete(task)
    loop.close()

