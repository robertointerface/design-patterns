"""Calculate if numbers are prime with Threading, as it can be seen if you run
this file as a python script, I run this with my razer blade and it takes me
36 seconds, while if you run the sequential code (that is not threads or
multiprocessors) it takes around 17 seconds.

So this shows how running heavy computational code by using threading is
actually much worse than doing this sequentially, this is due to the fact that
is all running under the same thread at the end also it takes more time
to manage all the thread, you need to create them and switch between threads,
while switching between threads you need to save registers, save stack pointer
(does that sound familiar to some of your university modules? saving stack pointers?)
so all this threading switching makes things go slower.
"""
from os import cpu_count

from concurrency.prime_number_calculation.calculate_prime_sequential import (
    PRIME_FIXTURE, is_prime)
from concurrent import futures
from datetime import datetime


def is_number_prime(prime_input: int):
    prime_number, expected_response = prime_input
    prime_res = is_prime(prime_number)
    assert prime_res == expected_response
    print(prime_number, prime_res)



if __name__ == "__main__":
    start_time = datetime.now()
    # simply run by using the ThreadPooExecutor, which is the simplest way
    # to run threads, if you set None on max_workers it will take the cpu_count().
    with futures.ThreadPoolExecutor(max_workers=cpu_count()) as executor:
        res = executor.map(is_number_prime, PRIME_FIXTURE)
    _ = list(res)
    print(f'it took {datetime.now() - start_time}')
