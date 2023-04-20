"""Here we can see an example of how to solve the argument limitation problem
that the executor.map function gives us, if we want to pass more than one
argument to the process function then we need to do as below and create each
process manually by using the method 'submit'.
"""

from time import perf_counter
from typing import NamedTuple
from concurrent import futures
from concurrency.prime_number_calculation.calculate_prime_sequential import (
    PRIME_FIXTURE,
    is_prime)


class PrimeResult(NamedTuple):  # <2>
    n: int
    flag: bool
    elapsed: float


def check(n: int, extra_arg) -> PrimeResult:
   # print(f'checking for prime on {n} with extra arg {extra_arg}')
    t0 = perf_counter()
    res = is_prime(n)
    return PrimeResult(n, res, perf_counter() - t0)


NUMBERS = [n for n, _ in PRIME_FIXTURE]

def main():
    workers = None
    # as before, use context manager.
    with futures.ProcessPoolExecutor(max_workers=workers) as executor:
        to_do_map = {}
        for number in sorted(NUMBERS):
            # first we create the process and they start executing right after
            # we submit them but keeping the limit of max workers.
            # notice how here we can actually pass more than one argument,
            # the first argument 'check' is the function that will be called
            # on the process, after that is all arguments, the function 'check'
            # in this case takes 2 arguments so we passed them.
            process = executor.submit(check, number, 'Mark')
            # save process on to do map, so you can inspect them if you want
            to_do_map[process] = number
        # 'futures.as_completed' method takes a list of processes and yields process
        # as they are being completed and have calculated a result. Use the method
        # to know which process have been finished or not.
        done_iter = futures.as_completed(to_do_map)
        # iterate over processes as they are finished
        for finished_process in done_iter:
            # you will notice that the 'state' of is always 'finished', if we
            # did not use futures.as_completed() then most likely we will get
            # some processes that have not yet finished and then we would not
            # be able to get a result yet.
            print(f'status for process {finished_process}')
            status = finished_process.result()
            prime = 'P' if status.flag else ''
            print(f'RESOLVED {status.n:16} {prime} {status.elapsed:9.6f}s')
        print(f'processes after completed {to_do_map}')

if __name__ == "__main__":
    main()



