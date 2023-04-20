# collections.namedtuple is a factory that builds subclasses of a tuple
# enhanced with field names.

from collections import namedtuple
City = namedtuple('City', 'name country population')
tokyo = City('Tokyo', 'JP', 36)
# friendly __repr__ tokyo City(name='Tokyo', country='JP', population=36)
print(f'tokyo {tokyo}')
# access fields with dot notation
print(f'tokyo population {tokyo.population}')
# access fields by index
print(f'tokyo population by index {tokyo[2]}')

# namedtuples also give you extra functionality
# use _fields
print(f'city fields {City._fields}')
# convert into a dictionary
print(f'tokyo as dictionary {tokyo._asdict()}')
