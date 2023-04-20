"""
most of the times you will work with the Task api, as asyncio.create_task(task)
runs a coroutine with create_task().

asyncio.Future() is a super class of 'Task' and allows you to interact with
the loop.

Future represents a future completion state of some activity and is managed by
the loop. basically a future is an instance of an activity that has not yet been completed but
in a future it will be completed.
"""
import asyncio

async def main(f: asyncio.Future):
    await asyncio.sleep(1)
    f.set_result('COMPUTER MAGIC!')

# we get the event_loop
loop = asyncio.get_event_loop()
fut = asyncio.Future()
print(f'future is done {fut.done()}')

# at this stage the task main is not running, is actually stopped, in order
# for it to run  we need to run the loop

task = loop.create_task(main(fut))
# we start running the loop
loop.run_until_complete(task)
print(f'future is done after running until complete {fut.done()}')
print(f'future result {fut.result()}')
