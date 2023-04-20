"""
asyncio library looks complex at first but keep in mind that you will most
likely only need to use a small portion of the library, asyncio has 2 types of
users.
1 - user that will just use asyncio for I/O data requests in async way.
2 - Framework creators.

Users of type 1 will get away with a basic understanding of the library and knowing
a few recipies, users of type 2 will need to know about manipulation the event
loop or handling OS signals.

Lest first answer some questions.
What is asyncio used for?
asyncio is a library to perform IO operations in an async manner, specially
https requests to api where most of the time you are just waiting for a response
but as we will see it can also be used in writing to files.

But we can already do that with threading, so why async?

1 - Asyncio is not faster than threading but makes possible to have hundred/thousands
of sockets listening at the same time, this is impossible with threading as threading
takes resources and each thread consumes about 8MB  so to have 1000 threads is 8GB of memory
just for threads management.

2 - the code is easier to read and follow, the code is easier to debug than the computer
magic of threading. But the code is harder to implement.
How to read async/await code, Guido gives a tip, he says that if you ignore
the async and await the code reads just as normal python code.

3 - as Async runs on a single thread you can minimize (not remove completely)
the race conditions and other non-deterministic behaviour of the thread computer magic.
The race conditions on variables on your code will be eliminated since we use
only one thread, BUT race conditions on external resources like external databases
is not eliminated, so be aware.

4 - The way threading chooses when to jump from thread to thread is by checking every 5ms
if it should jump to another thread because the current thread is waiting for I/O request,
One of the benefits of asyncio is that you exactly specify where the event loop needs
to jump to another task because the current one is 'waiting', that is the nice thing
about the keyword 'await' that you specify exactly to the event loop 'here we need to
wait so go do something else', instead of using multithreading that is constantly asking
'are you waiting? should I go do something else?'

lets remember the definition of a coroutine.

- Coroutine: A function that can suspend itself and come back when it desires
and is allowed.

how is async implemented in the low level?
async is just classic coroutines that in a very smart way manipulates the event_loop
of the single thread with multitasking management, it monitors the OS signals
and uses interrupts to manipulate the event_loop.
look at async_chapter/async_corouting_explanation.py for some experiments
on how async behaviour is very similar to coroutines.

what is the event_loop?
let's first answer, What is an event?
an event can be for example
- Functions returning a value.
- response from a http call.
- file IO event.
- sockets events.
basically events that happen in our code.
So the event loop is a loop (like a for loop) used by asyncio where you insert
functions and it performs those functions in a multitasking way but jumping back
and forward between those functions depending on events that are happening on those functions.
The loop can execute those functions, delay their execution, cancel them, it can do all this depending
on the events that are happening on those functions.

an event loop is started automatically when you start running a python async program,
with asyncio.run()
you can actually create your own event loop if you are interested.


look at event_loop/event_loop.py for a simple demonstration on how to manipulate event loop.
look at event_loop/infinite_event_loop.py for an example on how to manipulate the
event loop recursively.
look at block_event_loop.py for a demonstration on how the event loop can only execution
one task at the time.

*****************LOOK AT THE EVENT LOOP VIDEOS**************
If at this stage is not very clear what is the event loop I recommend you look
at the videos at edgedb online https://www.youtube.com/@EdgeDB/videos
specially the second video (https://www.youtube.com/watch?v=E7Yn5biBZ58) where
it talks about the loop in detail.

Talk is cheap lets see some code.
The most basic code of async can be seen on basic_async_code/most_basic_async_python.py
there we can see one of the most important concepts of async, async functions
need to have the keywords async and when executing async function you need
to use the word await.

Asyncio manipulates 'awaitable' objects,
what is an awaitable?
'for' loops work with iterables, 'await' works for 'awaitables'.

an awaitable is just a class that implements the __await__ method.

there are 2 types of awaitables.
1 - a native coroutine function, that is a function defined with 'async def'.
2 - asyncio.Task, you normally get this by passing a coroutine object to asyncio.create_task()

Let's look at some code.
Go to file async_chapter/flag_download_async.py for a quick example on how async
works and how you need to put 'async' on any function that will use await,
how any code that is async needs to be run on a root level with 'asyncio.run(async_function)'
and how comfortable is to use asyncio.gather(*awaitables) to just execute all
async coroutines together.

After looking at that code you can see the code on async_chapter/async_gather.py
and how important is for you to use it, otherwise you will not take all the advantages
of asyncio.

If you go to file async_chapter/flag_download_with_create_task.py you will
see a different way of running async coroutines, that is manually
starting the event loop and calling loop.create_task() to schedule the
tasks to be executed, then calling loop.run_until_complete(task).

so when do we use asyncio.run()/asyncio.gather(*awaitables) or
create tasks manually and run them?
It depends on the situations, if all you want is just to make a bunch of
IO calls and just want to be notified when all those calls have finished,
then just use asyncio.run()/asyncio.gather(*awaitables).
If you need more control over each async coroutine and you want to be notified
when each is finished or want to run them separately then use create_task().


Go to the file async_chapter/get_flag_semaphore.py and see how you can limit
the number of concurrent async functions running with asyncio.Semaphore.

One of the most important concepts that you need to understand about async is
you need to go full async or you are wasting your time, if one part of your code
that is doing IO operations is not using async then that can block the event
loop and you don't get all the benefits (or none) of async, BUT sometimes
blocking code is inevitable (like Thanos), for example you go and you create
super nice async code but you use aws botocore which is not async, so what do
you do in this case? well there is a solution for this, go to file flags_download/save_flags_async.py
where we deal with this.

Ok so you know how to run async code, you even know how to run threads and
processes inside your async code but life hits you hard and you are executing
a bunch of IO tasks on async way BUT one of the tasks fails while you still are
awaiting for other pending tasks to finish, so how do you handle this.
- do you let if finish the pending tasks?
- Do you stop all immediately and report error?

Well is up to you but you should know how to handle these cases. Look
at the code in flags_download/flags_download_take_care_of_errors.py for some
guidance.

################SPECIAL RECIPIES#######################################
1 - Contex Managers.
Sometimes you need connections to be opened and closed within well defined
scopes, that is when async context managers are handy
further_async_recipies/async_with_context_manager.py

2 - async iterator.
You can define your own async iterator the same way you can create your own
iterator, BUT instead of specifying the builtin methods __iter__ and __next__
you NEED to define __aiter__ and __anext__ (yes the extra 'a' is for 'async').
you can look at this recipe in further_async_recipies/async_as_iterator.py

3 - Async fo generators.
You can also define async generators, use further_async_recipies/async_generators.py


LAST BUT NOT LEAST:
If I raised your curiosity I give you here what I think are the best resources
for learing async.

1 - the async edgedb youtube videos are the best video-courses for async
in my opinion, they go deep https://www.youtube.com/@EdgeDB/videos

2 - there is a nice python async book,
https://www.amazon.co.uk/Using-Asyncio-Python-Understanding-Asynchronous/dp/1492075337/?_encoding=UTF8&pd_rd_w=a5kQG&content-id=amzn1.sym.ef3907ff-f91d-4263-9e4a-2471c52bf60e&pf_rd_p=ef3907ff-f91d-4263-9e4a-2471c52bf60e&pf_rd_r=FYEDNZE9MPWCR7WVB0VV&pd_rd_wg=9DiMs&pd_rd_r=6d8b8f4a-a243-4aa9-8ee3-cec5d64d9f2c&ref_=pd_gw_ci_mcx_mr_hp_atf_m

3 - as always the great David Beazly has a lot of content on his
 youtube channel https://www.youtube.com/@dabeazllc

"""
