"""Conftest is a special file on pytest, is a file dedicated to have fixtures
of scope 'package' or 'session' or fixtures that are used on multiple modules
or fixtures that are required on every test. Use conftest to define this
type of fixtures BUT do not over use it, DO NOT define all the fixtures
on conftest.
"""
import time

import pytest

# this is an example of a fixture that is called  as it has
# autouse=True.
@pytest.fixture(autouse=True, scope="session")
def footer_session_scope():
    "Prints a footer at the end of the session test"
    yield
    now = time.time()
    print('--')
    print(
        f"Finished: {time.strftime('%d %b %X', time.localtime(now))}"
    )
    print(f'--------------------')



@pytest.fixture(autouse=True, scope="function")
def footer_function_scope():
    "Prints a footer at the end of the session test"
    print(f'starting test')
    yield
    print(f'ending test')


