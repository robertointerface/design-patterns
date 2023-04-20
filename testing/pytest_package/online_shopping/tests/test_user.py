"""This tests simply include.
1 - test that values are correct
2 - test that an error is raised
"""

import pytest
from testing.pytest_package.online_shopping.errors import InvalidEmailError
from testing.pytest_package.online_shopping.user import User

# assert that an error is raised and that the error string response is equal
# to a given value
def test_user_invalid_email_raises_InvalidCardItemError():
    invalid_email = 'INVALID_EMAIL'
    with pytest.raises(InvalidEmailError, match=f"Invalid email {invalid_email}"):
        _ = User('name', invalid_email)


def test_user_email_set_when_correct():
    valid_email = 'validemail@email.com'
    user = User('name', valid_email)
    assert user.email == valid_email
