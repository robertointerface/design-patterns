from .errors import InvalidEmailError


class User:

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if '@' not in value:
            msg = f"Invalid email {value}"
            raise InvalidEmailError(msg)
        self._email = value
