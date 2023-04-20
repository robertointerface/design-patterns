"""Testing can be very repetitive sometimes, we try to test the same
function/functionality with multiple inputs, we can see that in the 3 tests
below and we can clearly see the repetitive pattern."""
import pytest


def convert_into_a_string(_input):
    return str(_input)

def test_convert_into_a_string_with_string():
    result = convert_into_a_string('string to test')
    assert isinstance(result, str)


def test_convert_into_a_string_with_integer():
    result = convert_into_a_string(5)
    assert isinstance(result, str)


def test_convert_into_a_string_with_float():
    result = convert_into_a_string(5.4)
    assert isinstance(result, str)

"""You say, ok that can be avoided with a simple for loop, yes? ok lets look
at that below. is much better but it brings other problem, we are testing
multiple scenarios under the same test, if one case fails is time consuming
to traceback which one failed, and if one case fails the rest of the cases will
not be tested.
"""

def test_convert_into_a_string():
    for c in ['string to test', 5, 5.5]:
        result = convert_into_a_string(c)
        assert isinstance(result, str)

"""But we can use pytest parametrization to avoid this repetition and not
have all the problems we had above, we have one test per test case, if one
test case fails the rest are tested also and tests are much more isolated. 
 
With parametrize fixture we can set multiple test scenarios, the test scenarios
need to be inside an iterable item like a list or a tuple, we need to specify
the name that the test case will take so we can pass it to the test function,
in this case we use the name 'test_case'"""
@pytest.mark.parametrize(
    'test_case',
    ['string to test', 5, 5.5])
def test_convert_into_string_parametrized(test_case):
    result = convert_into_a_string(test_case)
    assert isinstance(result, str)



def adder(a, b):
    return a + b
"""We can pass more than one argument per test, we do this in the test below"""
@pytest.mark.parametrize(
    'first_number,second_number,expected_result',
    [
        (1, 2, 3),
        (4, 6, 10),
        (2, 3, 8)
    ]
)
def test_adder(first_number,second_number,expected_result):
    result = adder(first_number, second_number)
    assert result == expected_result


"""you can also parametrize stacked, as below, you will see that 9 tests
are run to check all possible combinations"""

@pytest.mark.parametrize('first_param', (1, 2, 3))
@pytest.mark.parametrize('second_param', (6, 7, 8))
def test_dummy_to_show_stacked_parametrize(first_param, second_param):
    print(f'first param {first_param}')
    print(f'second param {second_param}')


