from .errors import InvalidCardItemError, ProductNotAvailableError
from .product_availability import check_product_availability


class Cart:

    def __init__(self):
        self.user = None
        self.items = []

    def set_user(self, user):
        self.user = user

    def add_item(self, item: 'CartItem'):
        """when you add an item to a cart you need to first verify 2 things.
        1 - is the item a cart item.
        2 - is the product available.

        if those 2 are meet then the items are added to the cart
        """
        if not isinstance(item, CartItem):
            raise InvalidCardItemError(f'invalid card item')
        if not check_product_availability(item.product_id, item.number_of_products):
            raise ProductNotAvailableError()
        self.items.append(item)

    def items_on_card(self):
        yield from self.items

    def user_name(self):
        return self.user.name


class CartItem:

    def __init__(self, product, number_of_products):
        self.product = product
        self.number_of_products = number_of_products

    @property
    def value(self):
        return self.product.product_value * self.number_of_products

    @property
    def product_id(self):
        return self.product.product_id

    @property
    def product_name(self):
        return self.product.name
