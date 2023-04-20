import pytest
from dataclasses import dataclass


@dataclass
class Footballer:
    goals: int


def assert_identical_players(p1: Footballer, p2: Footballer):
    # __tracebackhide__ is optional, if true it means that this function will
    # not be included on the fail traceback as is just visual noise
    __tracebackhide__ = True
    if p1.goals != p2.goals:
        pytest.fail(f"footballer not the same")


def dummy_function():
    a = 3
    breakpoint()
    b = 3
    c = 2
    f = c + [2, 2, 32]
    d = 2
    s = 'string'


def test_identical_footballers():
    messi = Footballer(23)
    cristiano = Footballer(21)
    dummy_function()
    assert_identical_players(messi, cristiano)
