from Class.Product import Product

class TshirtProduct(Product):
    tshirtcolor = None
    tshirtsize = None

    def __init__(self,
                 sku: str,
                 price: int,
                 name: str,
                 quantity: int,
                 brand: str,
                 tshirtsize: str,
                 tshirtcolor: str):
        super().__init__(sku, price, name, quantity, brand)
        self.tshirtsize = tshirtsize
        self.tshirtcolor = tshirtcolor

    def get_tshirtcolor(self):
        return self.tshirtcolor



    def Add_product(self, mongo_client) -> str:
        id = mongo_client.product.tshirt.insert_one({'Sku': self.sku,
                                                     'Price': self.price,
                                                     'Name': self.name, 
                                                     'Brand': self.brand,
                                                     'Quantity': self.quantity,
                                                     'TshirtColor': self.tshirtcolor,
                                                     'TshirtSize': self.tshirtsize})
        return id.inserted_id
    @staticmethod
    def Update_product(mongo_client, Sku, field, new_value):
        mongo_client.product.tshirt.update_one({'Sku': Sku}, {'$set': {field: new_value}})
    @staticmethod
    def Delete_product(mongo_client, Sku):
        mongo_client.product.tshirt.delete_one({'Sku': Sku})

    @staticmethod
    def find_product(mongo_client, sku):
        return mongo_client.product.tshirt.find_one({"Sku": sku})

    # def Print_data(self, mongo_client):
    #     result = mongo_client.product.tshirt.find()
    #     return result

