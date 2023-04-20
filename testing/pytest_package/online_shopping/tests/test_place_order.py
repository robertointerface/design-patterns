"""these tests are specially interesting for mocking examples.

1 - mock an external library like requests.
2 - assert that specific methods are called, is normal on applications that
by calling one function/method, this ends up calling other methods, in order
for you to test that a tree of methods is being called you need to use what
is called a 'spy' you can see this on test test_method_place_order_calls_all_required_methods

3 - assert functions are called with correct arguments, sometimes you want
to make sure that some functions are being called with correct arguments as
a function being called with correct arguments is essential, this can be seen
on test test_request_post_has_correct_payload_when_called_on_make_payment.

"""
import requests
import pytest
from pytest_mock import mocker

from testing.pytest_package.online_shopping.cart import CartItem, Cart
from testing.pytest_package.online_shopping.errors import \
    InvalidDeliveryAddress, InvalidPayment
from testing.pytest_package.online_shopping.place_order import OrderPlacer
from testing.pytest_package.online_shopping.product import Product
from testing.pytest_package.online_shopping.user import User


def mock_request_response(status_code, data):
    class MockRequest:
        def __init__(self, _status_code, _data):
            self.status_code = status_code
            self.data = data

    return MockRequest(status_code, data)


class TestOrderPlacer:

    @pytest.fixture
    def mock_request_to_reply_not_ok(self, mocker):
        # NOTE how here we use the mocker.patch.object
        requests_mocked = mocker.patch.object(requests, 'post')
        requests_mocked.return_value = mock_request_response(500, {})

    @pytest.fixture
    def mock_request_to_reply_ok(self, mocker):
        requests_mocked = mocker.patch.object(requests, 'post')
        requests_mocked.return_value = mock_request_response(200, {})


    @pytest.fixture
    def dummy_products(self):
        product_1 = Product(name="The lord of the rings",
                       price=10,
                       product_type='book',
                       product_id= "ABC")
        return [product_1]

    @pytest.fixture
    def dummy_user(self):
        return User(name='John Smith', email='jonhSmith@email.com')

    @pytest.fixture()
    def dummy_cart(self, dummy_products, dummy_user):
        items = []
        for product in dummy_products:
            cart_item = CartItem(product=product, number_of_products=1)
            items.append(cart_item)
        cart = Cart()
        cart.set_user(dummy_user)
        for item in items:
            cart.add_item(item)
        return cart


    def test_method_check_delivery_address_exists_raises_error_if_incorrect_address(self,
                                                                                    mock_request_to_reply_not_ok,
                                                                                    dummy_cart):
        delivery_address = '121 Wrong address alley'
        order = OrderPlacer(cart=dummy_cart, delivery_address=delivery_address)
        with pytest.raises(InvalidDeliveryAddress) as exc_info:
            order.check_delivery_address_exists()

    def test_method_make_payment_raises_InvalidPayment_if_payment_declined(self,
                                                                           mock_request_to_reply_not_ok,
                                                                           dummy_cart):
        delivery_address = '121 Wrong address alley'
        order = OrderPlacer(cart=dummy_cart, delivery_address=delivery_address)
        with pytest.raises(InvalidPayment, match='Invalid payment'):
            order.make_payment()


    # The example below is a good example when you want to assert that specific
    # methods are called, a good way to test the flow of the code
    def test_method_place_order_calls_all_required_methods(self,
                                                           mocker,
                                                           mock_request_to_reply_ok,
                                                           dummy_cart):
        # the one below you could also do with
        # spy_make_payment = mocker.patch.object(OrderPlacer, 'make_payment',
        #                                        side_effect=None)
        spy_make_payment = mocker.patch('testing.pytest_package.online_shopping.place_order.OrderPlacer.make_payment',
                                               side_effect=None)

        delivery_address = '121 Wrong address alley'
        order = OrderPlacer(cart=dummy_cart, delivery_address=delivery_address)
        order.make_payment()
        # use the built-in method assert_called_once, you have many more
        # methods like assert_called, or assert_called_with
        spy_make_payment.assert_called_once()

    # this test below is a very good example on how to test that a function
    # has been called with the expected arguments
    def test_request_post_has_correct_payload_when_called_on_make_payment(self,
                                                                          mocker,
                                                                          dummy_cart,
                                                                          dummy_user):
        # mock method post from package requests to make sure we are not calling
        # any api.
        requests_mocked = mocker.patch.object(requests, 'post')
        requests_mocked.return_value = mock_request_response(200, {})
        delivery_address = '121 Wrong address alley'
        order = OrderPlacer(cart=dummy_cart, delivery_address=delivery_address)
        cart_value = sum([item.value for item in dummy_cart.items])
        # call make_payment method which uses requets.post, we make sure that
        # requets.posts is called with the correct arguments that would be
        # necessary to get a valid answer from the requets.post method when
        # calling a valid http address.
        order.make_payment()
        requests_mocked.assert_called_with(
            url="Fake_address_to_get_if_address_is_real",
            headers='fake headers',
            data={
                'amount': cart_value,
                'user_name': dummy_user.name
            },
            # if you change the number 30 to any other you will see that the
            # test fails
            timeout=30
        )
