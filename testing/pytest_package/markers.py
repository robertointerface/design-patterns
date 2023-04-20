"""Markers are a way to tell pytest about something special about a particular
test, think of it as a tag, pytest gives us a good collection of builtin
 markers like parametrize that we already saw or we can create our own
 markers."""


"""Lets first look at the most useful builtin markers."""

import pytest
import datetime

"""Skip mark allows you the skip test and those tests will not be run, why 
do you want to skip a test? maybe the test is failing and you don't want to
run it until you can fix it or any other reason. """
@pytest.mark.skip(reason="this is a useless test")
def test_useless():
    assert 2 == 1


"""skipif mark allows us to skip a test if the specific condition we define
is met, the test below will only run on mondays and tuesdays, the other days
will be skip"""
@pytest.mark.skipif(
 datetime.datetime.today().weekday() >= 3,
 reason="test is only run mondays and tuesdays"
)
def test_if_skipping():
    assert 1 == 1


"""xfail, use xfail if you expect the test to fail, why then not mark it with 
skip? well this way the test will run and you will still be able to see why
it failed, it will just not be mark as a 'failure'."""

@pytest.mark.xfail(reason='XPASS demo')
def test_will_fail():
    assert "DOOM" == "QUAKE"

"""So what happens if we want to report as failure a test that is spected to 
fail but it passes, we would like to get notified of that, for those cases 
you can use the parameter 'strict'"""

# the test below will raise error as is expected to fail but it will not fail.
# the default of strict is False
@pytest.mark.xfail(reason='This will pass', strict=True)
def test_expected_to_fail_but_passes():
    assert "DOOM" == "DOOM"


"""you can also create your own custom markers, then you can dictate which
tests to run and which ones not to run, this is very useful if you want to 
run some tests for unit testing and other for integration testing.

to run tests with a specific mark use the m flag

pytest -m unittest

will run only the test with the mark 'unittest'.

DO NOT FORGET to set the markers on pytest.ini , is not mandatory but 
it will help.
"""

@pytest.mark.unittest
def test_some_function():
    assert 2 + 2 == 4


@pytest.mark.integration
def test_some_modules():
    assert 3 + 3 == 6

