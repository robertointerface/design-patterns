"""Here we use Multiprocessor to create multiple processors, we can clearly
see the benefit because it takes only around 5 seconds on my machine to compute
all the primes, much faster than the 17 seconds with sequential and 37 seconds
with threading.

In this example we use the executor.map function, this function takes care of
the problem of knowing when the process result is finished or not.

The only issue is that the executor.map function can only take one argument at
the time, for using more arguments we need to get messy.
"""
from concurrent import futures
from time import perf_counter
from typing import NamedTuple
from concurrency.prime_number_calculation.calculate_prime_sequential import (
    PRIME_FIXTURE,
    is_prime)
from datetime import datetime


class PrimeResult(NamedTuple):  # <2>
    n: int
    flag: bool
    elapsed: float

def check(prime_input) -> PrimeResult:
    number, _ = prime_input
    t0 = perf_counter()
    res = is_prime(number)
    return PrimeResult(number, res, perf_counter() - t0)


def main():
    # if we put None then the executor decides how many processes to use.
    workers = None
    # Initialize a process executor that takes care off
    executor = futures.ProcessPoolExecutor(workers)
    actual_workers = executor._max_workers
    print(f'Checking {len(PRIME_FIXTURE)} numbers with {actual_workers} processes:')
    t0 = datetime.now()
    numbers = PRIME_FIXTURE
    # use the executor as a context manager, WHY? well after all the processes
    # are finished we need to free all the memory used by the processors, for
    # this we need to call executor.shutdown(), by just using the context manager
    # we don't have to call shutdown() and our life is easier.
    with executor:
        # when we use executor map function all the problems of sharing resources
        # is handle by futures framework, here we create process, Processors
        # can be in 3 states:
        # 1 - pending: process is waiting for resources on the process pool executor
        # to be available so it can start.
        # 2 - running: process is running.
        # 3 - finished: process has finished its execution.
        # the __next__ method returns the process result as processes are being
        # finished (that is their status is finished), that is the beauty of
        # using the map function, it takes care of the problem on knowing or not
        # knowing when The process results are ready or not.
        # the executor map takes 2 arguments the first ('check' in this case) is
        # the computation that the process will be doing, this must be a reference
        # to the function the process will use to calculate the result, the
        # second argument (numbers in our case), is a list/tuple/array of inputs,
        # for each of the items on that list a process will be started where the
        # input to the specified function will be that item.
        for n, prime, elapsed in executor.map(check, numbers):
            label = 'P' if prime else ' '
            print(f'{n:16} {label}')
    time = datetime.now() - t0
    print(f'Total time: {time}')

if __name__ == '__main__':
    main()
