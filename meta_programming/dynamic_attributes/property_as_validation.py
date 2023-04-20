"""
You can also use properties to set getter and setter methods for specific
attributes and enforce rules on specific attributes.
"""

class AmazonOrder:

    def __init__(self, order_id, quantity, price):
        self.order_id = order_id
        self.quantity = quantity
        self.price = price

    def subtotal(self):
        return self.quantity * self.price


# so what happens to the above it the quantity is negative?
# opps is negative, believe or not this is a mistake that amazon actually
# did in it's beginning, people were putting negative quantities and they
# were getting credit on their accounts, true story.
order = AmazonOrder('2323', -2, 40)
print(f'order price {order.subtotal()}')


# To avoid the above problem we can define our own getters and setters

class AmazonOrder2:

    def __init__(self, order_id, quantity, price):
        self.order_id = order_id
        self.quantity = quantity
        self.price = price

    @property
    def quantity(self):
        # we return where the quantity is actually being saved, that is
        # under self._quantity
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value > 0:
            # the actual value is stored on self._quantity, which is not
            # self.quantity, self.quantity is the reference to the property
            self._quantity = value
        else:
            raise ValueError(f'quantity must be bigger than 0')

    def subtotal(self):
        return self.quantity * self.price

# if you run the line below you will see it raises errors
# order = AmazonOrder2('2323', -2, 40)

"""So we are all set, BUT wait a second, we are using property as a decorator,
as you are aware decorators are just functions that return other functions, what
if I told you that properties are actually classes. This is true, since at the
end of the day functions and classes are both callable, you call a function with
function() and you initialize a class with class(), as long as function() and 
class() return a new callable, there is really no difference."""

class AmazonOrder3:

    def __init__(self, order_id, quantity, price):
        self.order_id = order_id
        self.quantity = quantity
        self.price = price


    def quantity_getter(self):
        # we return where the quantity is actually being saved, that is
        # under self._quantity
        return self._quantity


    def quantity_setter(self, value):
        if value > 0:
            # the actual value is stored on self._quantity, which is not
            # self.quantity, self.quantity is the reference to the property
            self._quantity = value
        else:
            raise ValueError(f'quantity must be bigger than 0')

    def subtotal(self):
        return self.quantity * self.price
    # here we define the property directly using property class, this is actually
    # how it was done long long time ago in a galaxy far far away.
    quantity = property(fget=quantity_getter,
                        fset=quantity_setter,
                        fdel=None)

order = AmazonOrder3('2323', 3, 5)
print(f'order.quantity {order.quantity}')


"""Ok so either way we want to use the property validators, we now have a way
of not allowing negative quantities, but what about price? then we need to 
do the same for price and it looks like below AmazonOrder4, which looks very long and very
 repetitive, A sing of code smell is if you see very repetitive code."""


class AmazonOrder4:

    def __init__(self, order_id, quantity, price):
        self.order_id = order_id
        self.quantity = quantity
        self.price = price

    @property
    def quantity(self):
        # we return where the quantity is actually being saved, that is
        # under self._quantity
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value > 0:
            # the actual value is stored on self._quantity, which is not
            # self.quantity, self.quantity is the reference to the property
            self._quantity = value
        else:
            raise ValueError(f'quantity must be bigger than 0')

    @property
    def price(self):

        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            # the actual value is stored on self._quantity, which is not
            # self.quantity, self.quantity is the reference to the property
            self._price = value
        else:
            raise ValueError(f'quantity must be bigger than 0')

    def subtotal(self):
        return self.quantity * self.price
