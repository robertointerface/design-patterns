import asyncio
import time


async def main():
    print(f"{time.ctime()} Hello!")
    await asyncio.sleep(3)
    print(f"{time.ctime()} Goodbye!")

def blocking():
    print(f"{time.ctime()} Hello form a thread!")
    time.sleep(5)
    print(f"{time.ctime()} Hello form a finished thread!")

loop = asyncio.get_event_loop()
task = loop.create_task(main())
# if you call blocking from with just the function it will take the main
# thread and stop execution.
#blocking()
# if you call it with run_in_executor it will not block the main thread as
# it will basically create its own thread where to run blocking
#loop.run_in_executor(None, blocking)
loop.run_until_complete(task)

pending = asyncio.all_tasks(loop=loop)
for task in pending:
    task.cancel()
group = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)
loop.close()
