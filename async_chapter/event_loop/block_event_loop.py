"""Here we can see how the event loop can only run one function at the time
we use the function long_function to take control of the event loop and only
execute that."""
import asyncio
import datetime

def long_function():
    print('blocking event loop')
    for i in range(100_000):
        for j in range(10_000):
            pass


def print_now():
    print(datetime.datetime.now())

# trampoline is an infinite function, is constantly just printing the
# current date because it calls itself
def trampoline(name: str = ''):
    print(name, end=' ')
    print_now()
    #CALLING ITSLEF recursive
    loop.call_later(0.5, trampoline, name)


loop = asyncio.get_event_loop()
loop.call_soon(trampoline)
# here we see that when calling long_function the function trampoline stops
# printing and long_function blocks execution, this is a clear example of
# using async for a purpose that is not suitable.
#COMMENT ON PRESENTATION THE FUNCTION BELOW
loop.call_later(5, long_function)
loop.run_forever()




