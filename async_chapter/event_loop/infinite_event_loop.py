"""Here we just show how you can call the event_loop recursively, as in insert
"""
import datetime
import asyncio


def print_now():
    print(datetime.datetime.now())

def trampoline(name: str = ''):
    print(name, end=' ')
    print_now()
    # this function is running inside the event loop and we use it to insert
    # more functions to the event loop, notice how here we use get_running_loop
    # to get the current running loop as there can only be running one loop
    # at the time.
    running_loop = asyncio.get_running_loop()
    running_loop.call_later(0.5, trampoline, name)



loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.call_soon(trampoline)
loop.run_forever()

