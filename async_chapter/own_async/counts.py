import time
from collections import deque

class Scheduler:
    def __init__(self):
        self.ready = deque()
        self.sleeping = []

    def call_soon(self, func):
        self.ready.append(func)

    def call_later(self, delay, func):
        deadline = time.time() + delay # expiration time
        self.sleeping.append((deadline, func))
        self.sleeping.sort()

    def run(self):
        while self.ready or self.sleeping:
            if not self.ready:
                deadline, func = self.sleeping.pop(0)
                delta = deadline - time.time()
                if delta > 0:
                    time.sleep(delta)
                    self.ready.append(func)
                # find nearest deadline
            while self.ready:
                func = self.ready.popleft()
                func()

sched = Scheduler()


def count_down(n: int) -> None:
    if n > 0:
        print(f'Down: {n}')
       # time.sleep(1)
        sched.call_later(4, lambda: count_down(n-1))


def count_up(n: int, a=0)-> None:
    if a < n:
        print(f'up: {a}')
        #time.sleep(1)
        sched.call_later(1, lambda: count_up(n, a +1))

# sched.call_soon(lambda : count_up(20))
# sched.call_soon(lambda : count_down(5))
# sched.run()
import queue


class AsyncQueue:
    def __init__(self):
        self.items = deque()
        self.waiting = deque()
        self._closed = False

    def close(self):
        self._closed = True

    def put(self, item):
        if self._closed:
            raise ValueError
        self.items.append(item)
        if self.waiting:
            func = self.waiting.popleft()
            sched.call_soon(func)

    def get(self, callback):
        if self.items:
            callback(self.items.popleft())
        else:
            self.waiting.append(lambda : self.get(callback))


def producer(q, count):
    def _run(n):
        if n < count:
            print('producing', n)
            q.put(n)
            sched.call_later(60, lambda : _run(n+1))
        else:
            print('producer done')
            q.close()
    _run(0)



def consumer(q):
    def _consume(item):
        if item is None:
            print(f'consumer done')
            pass
        else:
            print('consuming', item)
            sched.call_soon(lambda : consumer(q))
    q.get(_consume)

q = AsyncQueue()
sched.call_soon(lambda : producer(q, 10))
sched.call_soon(lambda : consumer(q))
sched.run()
