"""Here we just show how we can manually insert functions on the event loop
and start execution the event loop.
here we just show how methods call_soon and call_later just insert functions
on the event loop queue but they are not started, the functions will only
start execution once we start the event loop with run_forever or
run_until_complete

"""
import datetime
import asyncio
def print_now():
    print(datetime.datetime.now())

# create a new event loop and set it as the default
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

# here nothing will happen as you need to run the loop.
# call soon is telling to call it immediately when it can
loop.call_soon(print_now)
# call later is providing a time to start, in this case is saying start
# after 1 second
loop.call_later(1, print_now)

# you can run the loop by running it forever or run until a specific task
# is complete, you can see
loop.run_forever()
# if below we sleep for less than 1 second we can see that the function on
# call later does not have time to start
#loop.run_until_complete(asyncio.sleep(3))
