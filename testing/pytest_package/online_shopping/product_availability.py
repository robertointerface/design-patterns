

AVAILABLE_PRODUCTS = []

def check_product_availability(product_id: str, number_of_products: int):
    for product in AVAILABLE_PRODUCTS:
        if (product['product_id'] == product_id
            and
            product['number_of_copies'] >= number_of_products):
            return True
    return False
