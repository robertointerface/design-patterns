

class Product:

    def __init__(self,
                 name: str,
                 price: float,
                 product_type: str,
                 product_id: str):
        self.name = name
        self.price = price
        self.product_type = product_type
        self.product_id = product_id

    @property
    def product_value(self):
        return self.price
