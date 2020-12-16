from Class.Product import Product


class SneakersProduct(Product):
    sneakerscolor = None
    sneakerssize = None

    def __init__(self,
                 sku: str,
                 price: int,
                 name: str,
                 quantity: int,
                 brand: str,
                 sneakerssize: int,
                 sneakerscolor: str):
        super().__init__(sku, price, name, quantity, brand)
        self.sneakerssize = sneakerssize
        self.sneakerscolor = sneakerscolor

    def get_sneakerssize(self):
        return self.sneakerssize
    
    def Add_product(self, mongo_client) -> str:
        id = mongo_client.product.sneakers.insert_one({'Sku': self.sku,
                                                     'Price': self.price,
                                                     'Name': self.name, 
                                                     'Brand': self.brand,
                                                     'Quantity': self.quantity,
                                                     'SneakersColor': self.sneakerscolor,
                                                     'SneakersSize': self.sneakerssize})
        return id.inserted_id

    @staticmethod
    def Update_product(mongo_client, Sku, field, new_value):
        mongo_client.product.tshirt.update_one({'Sku': Sku}, {'$set': {field: new_value}})

    @staticmethod
    def Delete_product(mongo_client, Sku):
        mongo_client.product.tshirt.delete_one({'Sku': Sku})
