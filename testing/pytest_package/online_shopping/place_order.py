import requests

from testing.pytest_package.online_shopping.errors import \
    InvalidDeliveryAddress, InvalidPayment


class OrderPlacer:

    def __init__(self, cart, delivery_address):
        self.cart = cart
        self.delivery_address = delivery_address

    def check_delivery_address_exists(self):
        # call fake request to verify address
        payload = {
            'address': self.delivery_address
        }
        delivery = requests.post(
            url="Fake_address_to_get_if_address_is_real",
            headers='fake headers',
            data=payload,
            timeout=30
        )
        if delivery.status_code != requests.codes.ok:
            msg = f"Delivery address {self.delivery_address} is not correct"
            raise InvalidDeliveryAddress(msg)

    def _get_cart_value(self):
        """Get the total sum of the cart items"""
        return sum([item.value for item in self.cart.items])

    def make_payment(self):
        # call fake request to make payment
        payload = {
            'amount': self._get_cart_value(),
            'user_name': self.cart.user_name()
        }
        delivery = requests.post(
            url="Fake_address_to_get_if_address_is_real",
            headers='fake headers',
            data=payload,
            timeout=30
        )
        if delivery.status_code != requests.codes.ok:
            msg = f"Invalid payment"
            raise InvalidPayment(msg)

    def place_order(self):
        steps = [self.check_delivery_address_exists,
                 self.make_payment]
        [step() for step in steps]
