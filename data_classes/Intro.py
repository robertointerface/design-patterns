"""Data classes is a way to build a simple class that is just a collection of
fields."""


# what are the benefits of using data class over traditional python class?
# lets start by showing limitations/problems that traditional dataclass gives
# us.
class Coordinate:

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


moscow = Coordinate(55.76, 37.62)
# you will see that the print statement is not very helpful as is something like
# <__main__.Coordinate object at 0x7f13c2f8df10>
print(f'print(moscow) = {moscow}')
# the == or __eq__ method compares object Ids
location = Coordinate(55.76, 37.62)
# this will be False as is comparing the Ids and not the lat and lon fields.
is_the_same_location = location == moscow
print(f'is_the_same_location = {is_the_same_location}')
# you can either modify the __eq__ method or compare by attribute
compare_by_attribute = (location.lat, location.lon) == (moscow.lat, moscow.lon)
print(f'compare_by_attribute = {compare_by_attribute}')

# So basically on traditional python class the following methods are not ideal.
# __repr__ : does not give us very helpful information.
# __init__ : a lot of boilerplate just to hold some data.
# __eq__ : compares Ids when we most likely want to compare class attributes.

# To the rescue comes Dataclass, dataclass implement methods __init__, __repr__
# __eq__ in a way that overcome the above limitations.
# Dataclass can be implemented in 3 different ways, namedtuple,
# typing.NamedTuple & decorator dataclass.
print('                                                                  ')
print('data class with namedtuple')
from collections import namedtuple
Coordinate = namedtuple('Coordinate', 'lat lon')
moscow = Coordinate(55.76, 37.65)
# the __repr__ is much more helpful printing "Coordinate(lat=55.76, lon=37.65)"
print(f'moscow as a tuple {moscow}')
location = Coordinate(55.76, 37.65)
# comparing with namedtuple compares the fields data lat and lon and
# location == moscow will give True
print(f'is the same location with named tuple = {location == moscow}')

print('                                                                  ')
print('data class with typing.NamedTuple')
import typing
# with NamedTuple you can set the typing
Coordinate = typing.NamedTuple('Coordinate', [('lat', float), ('lon', float)])
print(f'moscow as a typing.NamedTuple {moscow}')
location = Coordinate(55.76, 37.65)
# comparing with namedtuple compares the fields data
print(f'is the same location with named typing.NamedTuple = {location == moscow}')
# an added benefit of typing.NamedTyple is you can use typing methods like
# the below prints {'lat': <class 'float'>, 'lon': <class 'float'>}
print(typing.get_type_hints(Coordinate))

# you can also inherit from NamedTuple and override methods if you want

from typing import NamedTuple

class Coordinate(NamedTuple):
    lat: float
    lon: float

    def __str__(self):
        # you can override this method if you want
        pass
print('                                                                  ')
print('data class with decorator dataclass')

from dataclasses import dataclass
# you can also make it be immutable by doing @dataclass(frozen=True)
# and that way the user will not be able to modify it.
@dataclass()
class Coordinate:
    lat: float
    lon: float

    def __str__(self):
        # you can overwrite this one also
        pass
# WARNING
# for namedtuple or dataclass do not use __annotations__ attribute to get the
# type hints from the fields, instead use inspect.get_annotations(Class) or
# typing.get_type_hints(Class)





















