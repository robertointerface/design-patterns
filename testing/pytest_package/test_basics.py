import pytest
"""Here we will do basic tests using pytest to understand test methodology and
how to run tests using pytest CLI with the basic pytest CLI flags.
Test can be run with pytest by simply calling the command 'pytest' on the terminal.
Pytest will find all the files that start with test_<something> or that end
with <something>_test, then inside those files it will run as tests all the
functions that are named test_<something> or <something>_test or tests class that are named
Test<something>.


"""

# the test below is a silly test but it shows a very important flag on pytest
# that is the -v flag. If you simply run the test by calling command 'pytest',
# the following message will be displayed
"""

    def test_failing():
>       assert (1, 2, 3) == (2, 3, 1)
E       assert (1, 2, 3) == (2, 3, 1)
E         At index 0 diff: 1 != 2
E         Use -v to get more diff
"""
def test_failing():
    assert (1, 2, 3) == (2, 3, 1)

# if you include the flag -v (or --verbose) when calling pytest 'pytest -v'
# you will get a much better explanation of what is wrong. like below.
# this is one of the main advantages of pytest over unittest, the detail
# explanation of what failed on the test.
"""
    def test_failing():
>       assert (1, 2, 3) == (2, 3, 1)
E       assert (1, 2, 3) == (2, 3, 1)
E         At index 0 diff: 1 != 2
E         Full diff:
E         - (2, 3, 1)
E         + (1, 2, 3)

test_basics.py:6: AssertionError
"""
# when you run pytest with the CLI, first thing you will see on the terminal
# screen is the 'testing session' environment variables.
"""
platform linux -- Python 3.8.10, pytest-7.1.2, pluggy-1.0.0 -- /home/roberto-pupil/Desktop/pupil-projects/design_patterns/env/bin/python
rootdir: /home/roberto-pupil/Desktop/pupil-projects/design_patterns/testing/pytest_package

platform linux: this is a Linux thing.
Python 3.8.10, pytest-7.1.2, pluggy-1.0. : python, pytest version and dependent testing packages.
/home/roberto-pupil/Desktop/pupil-projects/design_patterns/env/bin/python: python interpreter location.
rootdir: /home/roberto-pupil/Desktop/pupil-projects/design_patterns/testing/pytest_package: this is the root directory,
top most common directory for all of the directories being searched for test code.
"""


# Test outcomes.
# 1 - PASSED (.): test run successfully.
# 2 - FAILED (f): test did not run successfully.
# 3 - SKIPPED (S): test was skipped by the users orders.
# 4 - xfial (x): Test was not suppossed to pass, ran and it did failed, sometimes
# you know that a test is going to fail so you mark it as it will fail and it
# this case it did failed so no problem there.
# 5 - XPASS (X): The test was not supossed to pass and it did pass so there
# is unexpected behaviour in this case.
# 6 - ERROR (E): an error happened outside of the testing function, most likely
# this error happened on the code that was being tested.

# there are many flags you can use when running pytest, if you type pytest --help
# you get all these flags but some of the most important are.

# -s : allows the coding print statements to be displayed, otherwise if you have
# prints they will not be shown.
# -x or --exitfirst: stop the testing immediately if any tests fails.

# -m: mark (see below for more).
# -k: expression (see below for more).


################# RUN TEST BY SEARCHING EXPRESSIONS ##################
# you can run some specific tests and not run other tests by using the -k flag
# is sort of a regex functionality, you give expressions to match and it will
# only run tests whose names match the given expression, for example if we
# run 'pytest -k "from_json or from_class" will only runt the tests test_init_from_json
# and test_init_from_class (will ignore the test named test_init_from_tuple),
# notice the logical 'or' and how you can use logical statements', this is a
# very powerful tool that can do much more, you can investigate more if you
# like.

def test_init_from_json():
    pass

def test_init_from_tuple():
    pass

def test_init_from_class():
    pass

# tests normally follow the pattern,
# 1 - prepare test arguments, environment...
# 2 - test the functionality you want to test.
# 3 - assert the functionality outcome was the expected

# for example lets say that you want to test an adder, no point on creating one
# but just for showing a simple example.
import numbers
def adder(a: numbers.Real, b: numbers.Real):
    return a + b

# so lets create a quick test for that

def test_adder_adds_as_expected():
    # prepare arguments, variables, environment...
    input_1 = 3
    input_2 = 5
    # test functionality
    result = adder(input_1, input_2)
    # assert functionality outcome is as expected
    assert result == 8

# some other very basic examples on testing can be seen on the example app on
# online_shopping














