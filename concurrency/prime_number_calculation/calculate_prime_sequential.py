from datetime import datetime
import math

PRIME_FIXTURE = [
    (2, True),
    (3, True),
    (142702110479723, True),
    (3333333333333301, True),
    (4, False),
    (3333333333333333, False),
    (3333335652092209, False),
    (4444444444444423, True),
    (4444444444444444, False),
    (4444444488888889, False),
    (5555553133149889, False),
    (5555555555555503, True),
    (5555555555555555, False),
    (6666666666666666, False),
    (6666666666666719, True),
    (6666667141414921, False),
    (7777777536340681, False),
    (7777777777777753, True),
    (7777777777777777, False),
    (9999999999999917, True),
    (9999999999999999, False),


]

NUMBERS = [n for n, _ in PRIME_FIXTURE]

# tag::IS_PRIME[]

def is_prime(n: int) -> bool:
    """Calculates if a number is prime or not, that is the number is only
    divisible by itself and 1, i.e 3"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    root = math.isqrt(n)
    for i in range(3, root + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    t0 = datetime.now()
    # iterate over all the prime numbers and calculate if they are prime or
    # not, assert the result is as expected.
    for n, prime in PRIME_FIXTURE:
        prime_res = is_prime(n)
        assert prime_res == prime
        print(n, prime)
    # calculate the time it took to calculate all prime numbers in a sequential
    # way, that is no threading or no multiprocessor, the time will vary on
    # the device but on my razer blade 9 core I get around 20 secs +- 10%
    print(f'it took {datetime.now() - t0} on sequential')
