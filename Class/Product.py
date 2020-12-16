class Product(object):
    sku = None
    price = None
    name = None
    brand = None
    quantity = None

    def __init__(self,
                 sku: str,
                 price: float,
                 name: str,
                 quantity: int,
                 brand: str):
        self.sku = sku
        self.price = price
        self.name = name
        self.quantity = quantity
        self.brand = brand

    def get_price(self):
        return self.price
    def get_sku(self):
        return self.sku
    def get_name(self):
        return self.name
    def get_quantity(self):
        return self.quantity
    def get_brand(self):
        return self.brand