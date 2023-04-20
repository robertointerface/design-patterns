import asyncio
import inspect

async def just_wait():
    await asyncio.sleep(3)
    print('finished awaiting')

print(f"type of just_wait {type(just_wait)}")
coro = just_wait()
# you can see coro is of type coroutine
print(f'type of coro {type(coro)}')
loop = asyncio.get_event_loop()
# create a task schedules a task to be run on the provided loop, it does not
# start its execution but schedules it.
task = loop.create_task(coro)
print(f'task type {type(task)}')
