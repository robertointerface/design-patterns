"""
These tests are interesting for:

1 - it emphasizes the importance of mocking where the component is used and
not where is created, this is on test test_add_item_raises_ProductNotAvailableError
"""
import pytest
from pytest_mock import mocker
from testing.pytest_package.online_shopping.errors import \
    ProductNotAvailableError, InvalidCardItemError
from testing.pytest_package.online_shopping.cart import Cart, CartItem
from testing.pytest_package.online_shopping.product import Product


class TestCart:

    def test_add_item_raises_ProductNotAvailableError(self, mocker):
        # In order for ProductNotAvailableError to be raised, the check_product_availability
        # method needs to return False, This depends on the attribute AVAILABLE_PRODUCTS
        # In this test we only want to test the fact that the error ProductNotAvailableError
        # is raised, we don't care about the rest, that is why the easiest way
        # to test this is to mock the method check_product_availability and make
        # it return False, Note below that when defining the mocking path we
        # use where check_product_availability is used and not where is defined.
        mocker.patch('testing.pytest_package.online_shopping.cart.check_product_availability',
                     return_value=False)
        cart = Cart()
        product_to_test = Product(name='testing product',
                                  price=12.24,
                                  product_type='testing type',
                                  product_id='342')
        card_item = CartItem(product=product_to_test, number_of_products=2)
        with pytest.raises(ProductNotAvailableError):
            cart.add_item(card_item)

    def test_add_item_raises_InvalidCardItemError(self):
        cart_item = 'this is a string and therefore is not of type CartItem'
        cart = Cart()
        # note how in this way we get
        with pytest.raises(InvalidCardItemError) as exec_info:
            cart.add_item(cart_item)
        assert exec_info.value.args[0] in 'invalid card item'

    def test_add_item_appends_item_when_is_correct(self):
        cart = Cart()
        product_to_test = Product(name="Harry Potter",
                                  price=15.80,
                                  product_type="book",
                                  product_id="ABD")
        cart_item = CartItem(product_to_test, 1)
        cart.add_item(cart_item)
        # assert there is at least one item with that name
        assert any([item.product_name == product_to_test.name for item in cart.items_on_card()])
