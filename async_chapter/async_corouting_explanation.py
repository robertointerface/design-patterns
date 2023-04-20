"""Here we just want to show how asyncio under the hood is just automating
the process of send(), yield() and StopIteration to run and switch between
coroutines"""
import asyncio



def normal_coroutine():
    print("inside normal_coroutine")
    value = yield 123
    return value + 2

def normal_coroutine_2():
    print("inside normal_coroutine_2")


async def f_no_await():
    print("inside f_no_await")
    return 123


async def f_with_await():
    print(f'before sleep')
    await asyncio.sleep(0) # we need to set 0 here
    print(f'after sleep')
    return 123


async def main():
    result = await f_with_await()
    return result


async def main2():
    coro = await f_with_await()
    print(f'before sending')
    result = coro.send(None)
    print(f'result {result}')

# EXAMPLE 1 NORMAL COROUTINE
# just show how a coroutine stops the event loops and allows you defined when
# a function is stopped and when you can continue its execution
# coro = normal_coroutine()
# print(f'after init coroutine')
# try:
#     first_yield = next(coro)
#     print(f"first_yield {first_yield}")
#     result = coro.send(2)
# except StopIteration as e:
#     print(f"result from normal coroutine {e.value}")


# EXAMPLE 2
# see how async is just a complex coroutine where
# coro = f_no_await()
# print(f'before try, f_no_wait already initialized')
# try:
#     coro.send(None)
# except StopIteration as e:
#     print(f'iteration stopped {e.value}')

# EXAMPLE 3
# test f_with_await show how the await is similar to a coroutine
# coro = f_with_await()
# print(f'before try, f_with_await already initialized')
# try:
#     print(f'before send')
#     coro.send(None)
#     print(f'after sending')
#     # if we comment the line below we see the StopIteration is never reached and
#     # the function does not return anything
#     coro.send(None)
# except StopIteration as e:
#     print(f'iteration stopped {e.value}')

# EXAMPLE 4
# show how we can let the send() method be controlled by asyncio and we get the same result.
# internally, the method 'run_until_complete' is just doing the send(None) calls for you and detects the
# StopIteration and returns you the value
# loop = asyncio.get_event_loop()
# coro = f_with_await()
# result = loop.run_until_complete(coro)
# print(f'result {result}')
