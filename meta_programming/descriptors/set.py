
class ParentOrder:

    def __getattribute__(self, item):
        print(f'inside ParentOrder __getattribute__')
        raise AttributeError


class Order:

    def __init__(self, price):
        self.price = price

    def __get__(self, item):
        print(f'inside __get__')

    def __getattr__(self, item):
        print(f'inside Order __getattr__')

    def __getattribute__(self, item):
        print(f'inside Order __getattribute__')
        raise AttributeError

    def non_special_attribute(self):
        pass
    # def __setattr__(self, key, value):
    #     print(f'inside __setattr__')

order_class = Order(3)
print(f'class vars {vars(Order)}')
print(f'instance vars {order_class}')
#print(f'order.price {order_class.price}')
