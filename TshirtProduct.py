from  Product import Product

class TshirtProduct(Product):
    tshirtcolor = None
    tshirtsize = None

    def __init__(self, console=False):
        super().__init__(console)
        if console:
            print('Введите  tshirtcolor')
            self.tshirtcolor = input()
            print('Введите  tshirtsize')
            self.tshirtsize = input()


    def Add_product(self, mongo_client) -> str:
        id = mongo_client.product.tshirt.insert_one({'Sku': self.sku,
                                                     'Prise': self.prise,
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

    # def Print_data(self, mongo_client):
    #     result = mongo_client.product.tshirt.find()
    #     return result

