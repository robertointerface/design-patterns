"""
Why fixtures should be used?
1 - Sometimes tests need preparations before the test can be started, like
mocking a database or connecting to database, opening files and so on, keep in mind
that tests should be kept as simple as possible and only essential code should
be inside the test function, fixtures allow us to create these 'preparations'
outside of the tests and that way we keep the tests simple.

2 - Our tests should only fail if the functionality that we want to test fails.
What happens if an error happens on the tests 'preparations', then we have a
fail, but the functionality that we want to test has not failed, what failed is
the test preparations, we then have a false failure.
If errors happen inside a fixture, this is displayed as 'Error' and
not as 'fail', if an error happens inside a testing function (I mean error not
assert failure) like TypeError, this is displayed as Fail, this makes it easier
to debug your tests.
"""
import pathlib
import json
import os
import pytest

# lets see an example of when to use fixtures, supose we want to test if data is present on a
# file (computer_science_courses.json)
"""The problem is that loading the data is not related to the test itself, we
can put this outside"""
def test_all_courses_have_lecturer():
    with open('./computer_science_courses.json', 'r+') as f:
        data = json.load(f)
        for course in data.get("Courses"):
            assert 'Lecturer' in course




# 'scope' argument: specify when the fixture will run, i.e module means will run once per
# module and all the tests that use it on that module will take the same yield,
# this is useful if the fixture is very time consuming and we don't want it to
# be executed for every test that uses it. You can set different scopes, look
# at the documentation for details on all of them.

@pytest.fixture(scope="module")
def load_data_from_database():
    with open('./computer_science_courses.json', 'r+') as f:
        data = json.load(f)
        print(f'this is executed before the test function, this is test setup')
        yield data
        # this will run independently if the test failed, raised error or not.
        print("this is executed after the test function, this is test teardown")


# we just pass the fixture as an argument, the test function is easier
# to read
def test_all_courses_have_name(load_data_from_database):
    print('execution test')
    for course in load_data_from_database.get("Courses"):
        assert 'name' in course

"""Fixtures can use other fixtures, but fixtures can only use fixtures that
have the same scope or higher, i.e a class scope fixture can use other class
scope fixtures or module fixture BUT can not use a function
scope fixture because function is one level down from class"""


"""Fixtures scope can also be define dynamically"""

def get_fixture_scope():
    if os.environ.get('user') is not None:
        return 'class'
    return 'function'

@pytest.fixture(scope=get_fixture_scope())
def load_data_from_database_2():
    with open('./computer_science_courses.json', 'r+') as f:
        data = json.load(f)
        print(f'this is executed before the test function, this is test setup')
        yield data
        # this will run independently if the test failed, raised error or not.
        print("this is executed after the test function, this is test teardown")



"""If you have fixtures that are required to be called on every test, then
set autouse=True, these types of fixtures should be define on conftest.py
"""


"""Sometimes fixtures names become too long and it becomes ugly to use them
as input to functions, in that case you can rename the fixture like below."""

@pytest.fixture(name='ultimate_answer')
def ultimate_answer_fixture():
    return 42

def test_dummy(ultimate_answer):
    assert ultimate_answer == 42



