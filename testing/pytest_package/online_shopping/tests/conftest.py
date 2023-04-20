"""this conftest file shows fixtures that are required on multiple tests and
one that is called for all the tests."""
from pathlib import Path
import pytest
import json
from testing.pytest_package.online_shopping.product_availability import AVAILABLE_PRODUCTS

AVAILABLE_PRODUCTS_FILE = Path(__file__).parent / 'test_data' / 'available_products.json'


@pytest.fixture
def warehouse_products():
    record_file = open(AVAILABLE_PRODUCTS_FILE)
    yield json.load(record_file)
    record_file.close()


# the fixture below needs to be called on all the tests as in order to test
# our online app we need to have a fictitious warehouse with products.
# also see how fixtures can use other fixtures.
@pytest.fixture(autouse=True)
def load_online_warehouse_products(warehouse_products):
    for item in warehouse_products:
        AVAILABLE_PRODUCTS.append(item)


