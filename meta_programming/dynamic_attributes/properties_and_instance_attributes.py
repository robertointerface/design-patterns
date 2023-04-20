# On must differentiate between instance attributes and class attributes,
# class Attributes belong to the class and instance attributes belong to a
# specific instance and can be different on an instance basis while class
# attributes are the same on all instance (but as we will see down is more
# complex as instance attributes can override class attributes)
class Class:
    # this is a class attribute
    data = 'the class data attr'

    def __init__(self, _instance_attribute):
        self._instance_attribute = _instance_attribute

    # this is a class attribute
    @property
    def prop(self):
        return 'the prop value'

# How can you access instance attributes?
class_instance = Class('instance atrib')
# if you use vars with the instance you can get the instance attributes
# note that with the line below you will NOT get 'data'
print(f'instance attributes using vars = {vars(class_instance)}')
# you can also use __dict__ since __dict__ is how you store the instance
# attributes
print(f'use __dict__ to get instance attributes= {class_instance.__dict__}')
# you can add instance attributes on they fly with dot notation
class_instance.new_attribute = 'this is a new attribute'
print(f'updated instance attributes {vars(class_instance)}')
# you can also take advantage of __dict__ and just add attributes as if you
# are just updating a dictionary. You must do it through __dict__, don't
# try to do directly like class_instance['extra_new_attribute'] unless you
# have set something special under the hood.
class_instance.__dict__['extra_new_attribute'] = 'new attribute with dict'
print(f'updated instance attribute with __dict__ {vars(class_instance)}')
# what about class attributes
print(f'class attributes with vars = {vars(Class)}')
# what about updating class attributes?
# is the same concept, you can use dot notation
Class.new_class_attribute = 'new class attribute'
print(f'class attributes after updating {vars(Class)}')


"""One thing to keep in mind is that class attributes are the same on all class
instances."""

class1 = Class('instance attribute for class 1')
class2 = Class('instance attribute for class 2')
print(f'class1 class attribute {class1.data}')
print(f'class2 class attribute {class2.data}')

# what happens if we just change the class attribute on the class itself.
Class.data = 'New modified class attribute'
# here we can see it has changed for both class instances as they all share
# the same reference.
print(f'class1 class attribute after modified {class1.data}')
print(f'class2 class attribute after modified {class2.data}')
