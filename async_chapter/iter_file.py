NUMBERS = [1, 2, 3, 4]
index = 0
import sys

def __iter__():
    return sys.modules[__name__]


def __next__():
    global index, NUMBERS
    index += 1
    return NUMBERS[index]
