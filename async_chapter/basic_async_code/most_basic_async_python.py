import asyncio
"""
WHAT TO LOOK FOR:
- Async code needs to be started with asyncio.run(), notice how asyncio.run()
takes care of all the event_loop management, you don't need to do anything.
when you start executing main() function you already have an event loop started
and when all is finished is automatically closed for you.
- Async functions need to have 'async' and use 'await' to wait for a promise/future
"""

# async functions need to start with 'async'
async def main():
    # we need to use 'await' to stop executing code inside the 'async' block
    # until we get a response and execute other async functions in the meantime
    # while we wait for a response.
    await asyncio.sleep(2)


if __name__ == "__main__":
    # use asyncio.run() to start executing 'async' code
    # NOTE that if you just call the function main() it will not run
    asyncio.run(main())
