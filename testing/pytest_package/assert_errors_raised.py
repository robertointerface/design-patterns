"""
Applications will fail, in those cases we normally catch the errors and handle
them. In order to know that the errors are handled correctly we need to
create the conditions for those errors to raise and assert they have risen.
That is why is important this topic.
"""
import pytest
from dataclasses import dataclass


@dataclass
class Footballer:
    goals: int

"""for example we want to assert that TypeError is raised if we try to initalize
a dataclass with not all the required arguments"""
def test_raises_when_missing_field():
    with pytest.raises(TypeError):
        messi = Footballer()


"""We can also test that the error message is the desire one"""
def test_raises_when_missing_field_with_argument():
    # test also that the message is the desire one
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'goals'"):
        _ = Footballer()


def test_raises_with_info():
    # you can also grab the exception info and analyze it.
    with pytest.raises(TypeError) as exc_info:
        messi = Footballer()
    expected = "missing 1 required positional argument: 'goals'"
    assert expected in str(exc_info.value)
