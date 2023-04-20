import asyncio
import socket
from keyword import kwlist
from typing import Tuple
MAX_KEYWORD_LEN = 4
NAMES = (kw for kw in kwlist if len(kw) <= MAX_KEYWORD_LEN)
import time

async def probe(domain: str) -> Tuple[str, bool]:
    loop = asyncio.get_running_loop()
    try:
        await loop.getaddrinfo(domain, None)
    except socket.gaierror:
        return (domain, False)
    return (domain, True)


async def main():

    domains = (f'{name}.dev'.lower() for name in NAMES)
    coros = [probe(domain) for domain in domains]
    for coro in asyncio.as_completed(coros):
        # at this point the coro is completed but we still need to use the
        # await to get the result, if coro raised an expection it would be
        # re-raised here
        domain, found = await coro
        mark = '+' if found else ' '
        print(f'{mark} {domain}')


if __name__ == "__main__":
    t0 = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - t0
    print(f'downloads in {elapsed:.2f}s')
