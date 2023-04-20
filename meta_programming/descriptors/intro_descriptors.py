"""descriptors are a way of reusing the same access logic in multiple
attributes, some industry examples are Django Object Relational Mappers or
the widely used SQLAlchemy package.


"""

# this is a classical attribute Descriptor implementation.
class OrderValidator:

    def __init__(self, validator_name):
        self.validator_name = validator_name

    # __set__ will be called when there is an attempt to assign a value
    # - self refers in this case to the attribute descriptor (OrderValidator) instance
    # - 'instance' is AmazonOrder instance
    # - 'value': is the value being assigned.
    def __set__(self, instance, value):
        if value > 0:
            # use the fact that all instance (not class) attributes are stored
            # under the instance.__dict__ to save the attribute
            # DO NOT do
            # setattr(instance, value)
            # as that would just trigger __set__ again and you are in an infinite
            # loop.
            instance.__dict__[self.validator_name] = value
        else:
            raise ValueError(f'quantity must be bigger than 0')

    def __get__(self, instance, owner):
        return instance.__dict__[self.validator_name]


class AmazonOrder:

    # in this case it uses descriptor instances, keep in mind that these 2 below
    # are class attributes, so they will be the same on all AmazonOrder instances
    # as class attributes are the same on all instances
    quantity = OrderValidator('quantity')
    right_price = OrderValidator('price')

    def __init__(self, order_id, quantity, price):
        # this will run only when you instantiate the class
        print(f'inside __init__ with quantity={quantity} price={price}')
        self.order_id = order_id
        # here self.quantity references to the class attribute above, but remember
        # that class attribute is the attribute descriptor and under the hood
        # will actually manipulate the instance attribute.
        self.quantity = quantity
        self.right_price = price

    def subtotal(self):
        return self.quantity * self.right_price


