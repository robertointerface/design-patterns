"""
Here we implement dynamic attributes by creating a FrozenJSON class which it
replicates the way we access data on a json object with javascript language.

This is to navigate through a dictionary with attributes, so instead of getting nested
dictionary values by using notation my_dict[name1][name2][name3], you can do
like my_dict.name1.name2.name3 (like in javascript).

We do this by implementing our own method __getattr__.

When you try to access an attribute on an object my_object.x it first looks
at my_object instance has an attribute called x, if not it searches my_obj.__class__
to see if is a class attribute, if not found as a class attribute then it calls
__getattr__.
"""
import json
from collections import abc


class FrozenJSON:

    def __init__(self, mapping: abc.Mapping):
        self.__data = dict(mapping)

    def __getattr__(self, name):
        print(f'inside __getattr__ for name={name}')
        try:
            # try to see if the name is an attribute
            return getattr(self.__data, name)
        except AttributeError:
            print(f'name = {name} not found as an attribute, building it'
                  f'with frozen json')
            # make sure you do self.__data, otherwise if you do self.data
            # you will get in an infinite loop.
            # Make sure you return the new created instance already initialized
            # otherwise you will not be able to concatenate attributes like
            # my_instance.attrib_1.attrib_2.attrib_3
            return FrozenJSON.build(self.__data[name])

    def __dir__(self):
        return self.__data.keys()

    @classmethod
    def build(cls, obj):
        # if the object is a dictionary or similar, then just initialize
        # the same way as FrozenJson
        if isinstance(obj, abc.Mapping):
            print(f'building dictionary {obj}')
            return cls(obj)
        # if is a list, then you need to initialize a list of ForzenJson
        elif isinstance(obj, abc.MutableSequence):
            print(f'building list of objects')
            return [cls.build(item) for item in obj]
        else:
            print(f'just returning object {obj}')
            return obj


if __name__ == "__main__":
    file = open('./oscon.json')
    # initialize FrozenJson with json data from oscon.json which just contains
    # data about events happening on a python conference
    frozen_obj = FrozenJSON(json.load(file))
    # now we try to access data Schedule.conferences[0].serial FrozenJson will
    # try to find 'schedule' with the following steps.
    # 1 - FrozenJson looks if it has an attribute with that name.
    # 2 - If the class does not have an attribute with that name then it looks
    # at parent classes (if any).
    # 3 - if no parent classes has that attribute then it calls special method
    # __getattr__
    # and get the 'conferences' (which is
    # a list), we use index 0 to get the first item on conference.
    serial = frozen_obj.Schedule.conferences[0].serial
    # if we try to access like below we would get an error since conferences
    # is a list of FrozenJson and not a FrozenJson object
    serial_1 = frozen_obj.Schedule.conferences.serial
    print(f'serial {serial}')
