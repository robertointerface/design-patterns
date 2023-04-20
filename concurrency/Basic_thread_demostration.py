import itertools
import time
from threading import Thread, Event


# This function just prints the message msg with a spinner line
def spin(msg: str, done: Event) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}' # \r moves the message to the start of the line
        print(status, end='', flush=True)
        if done.wait(.1):
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')

def slow() -> int:
    time.sleep(.5)
    return 42


def supervisor() -> int:
    # Event class is the simplest mechanism to coordinate threads,
    # Event has an internal attribute 'flag' that is initialized to False,
    #
    done = Event()
    spinner = Thread(target=spin, args=('thinking!', done))
    print(f'spinner objects: {spinner}')
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result
