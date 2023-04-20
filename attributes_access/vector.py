from typing import List

"""We use __getattr__ to access vector points by name instead of having to
access them by index"""


class Vector:

    __match_args__ = ('x', 'y', 'z')

    def __init__(self, points: List):
        self._points = points

    def __getattr__(self, name):
        cls = type(self)
        try:
            pos = cls.__match_args__.index(name)
        except ValueError:
            pos = -1
        if 0 <= pos <= len(self._points):
            return self._points[pos]
        raise AttributeError(f'point with name {name} does not exist')



if __name__ == "__main__":
    v1 = Vector([1, 2, 3])
    print(f'v.x = {v1.x}')

