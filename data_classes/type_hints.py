# type hints or type annotations are ways to declare the expected type of
# function arguments, return values, variables and attributes.

# first thing to mention is that type hints are not enforced by python compiler
# or interpreter

import typing
class Coordinate(typing.NamedTuple):
    lat: float
    lon: float
# not enforced Coordinate is expecting float types but we give String types
# (maybe you get a hint from pycharm or your linter)
trash = Coordinate('String', 'string')
print(f'trash = {trash}')

# PEP 484 describes acceptables types

# We can provide as typing built-in types, callables or class, sequences of
# types.. acceptable type hints
# https://peps.python.org/pep-0484/#acceptable-type-hints
class DragonBallClass:
    pass

class DemoPlainClass:
    a: int # annotation with no default
    b: DragonBallClass # annotate with a class
    c: typing.List[int] # annotate with a list of integer
    d: typing.Union[int, float] # can be both int or float
    e: float = 1.1 # annotation with default
    f = 'spam' # no annotation, old school attribute


# if you run the below statement you will see it will raise an error, this
# is because when you don't define a default it does not set it as an attribute
# accessing 'a' will raise AttributeError as is not defined yet
#print(f'DemoPlainClass.a {DemoPlainClass.a}')

# but when you define a default on it, then it sets an attribute for it
print(f'DemoPlainClass.e {DemoPlainClass.e}')



from dataclasses import dataclass

@dataclass
class DemoDataClass:
    a: int
    b: float = 1.1
    c = 'spam'

# get the annotations {'a': <class 'int'>, 'b': <class 'float'>}
print(f'DemoDataClass.__annotations__ {DemoDataClass.__annotations__}')
# get the doc DemoDataClass(a: int, b: float = 1.1)
print(f'DemoDataClass.__doc__ {DemoDataClass.__doc__}')






