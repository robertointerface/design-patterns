
print(f'You are runing module property_factory.py and DC universe sucks lets face it')
def order_validator(validator_name):

    # instance = self
    def validator_getter(instance):
        return instance.__dict__[validator_name]

    # instance = self when we use the setter
    def validator_setter(instance, value):
        print(f'setting {validator_name} for instance = {instance} value = {value}')
        if value > 0:
            # use the fact that all instance (not class) attributes are stored
            # under the instance.__dict__ to save the attribute
            instance.__dict__[validator_name] = value
        else:
            raise ValueError(f'quantity must be bigger than 0')

    return property(fget=validator_getter, fset=validator_setter)


class AmazonOrder:
    # you will see that this is runs before everything, this is because when
    # you import or run this module/file/script it first builds the components
    # inside the module/file, in this case it builds the class AmazonOrder, not
    # the instance but the class, it builds it so that it can be used.
    print(f'setting class attributes')
    quantity = order_validator('quantity')
    price = order_validator('price')

    def __init__(self, order_id, quantity, price):
        # this will run only when you instantiate the class
        print(f'inside __init__ with quantity={quantity} price={price}')
        self.order_id = order_id
        # here self.quantity references to the class attribute above, but remember
        # that class attribute is a property and under the hood will actually
        # manipulate the instance attribute.
        self.quantity = quantity
        self.price = price

    def subtotal(self):
        return self.quantity * self.price


order = AmazonOrder('2323', 2, 10)
