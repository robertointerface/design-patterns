"""This is a good example on how to use parametrize mark to avoid duplicated
code."""

import pytest

from testing.pytest_package.online_shopping.cart import CartItem
from testing.pytest_package.online_shopping.product import Product
from testing.pytest_package.online_shopping.product_availability import check_product_availability



@pytest.mark.parametrize('product_id,number_products,expected_result',
                         (
                             ("ABC", 1, True),
                             ('NOT_VALID_ID', 1, False),
                             ("XYZ", 15, False)
                         ))
def test_check_product_availability(product_id, number_products, expected_result):
    is_available = check_product_availability(product_id, number_products)
    assert is_available == expected_result


def test_cart_item_product_value_property():
    product = Product(name='lord of the rigns',
                       price=10,
                       product_type='book',
                       product_id='12324')
    item = CartItem(product, 3)
    assert item.value == 30

def test_cart_product_id_property():
    product_id = '12324'
    product = Product(name='lord of the rigns',
                       price=10,
                       product_type='book',
                       product_id=product_id)
    item = CartItem(product, 3)
    assert item.product_id == product_id
