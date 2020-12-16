from Class.TshirtProduct import TshirtProduct
from Class.SneakersProduct import SneakersProduct


class Command(object):
    list_product = ['Tshirt', 'Sneakers']
    list_command = [
        'add_good',
        'stop',
        'delete_good',
        'update_good'
    ]


    def execute_command(self, run_command, client):

        if run_command == 'add_good':
            self.add_good(client)

        if run_command == 'delete_good':
            self.delete_good(client)

        if run_command == 'update_good':
            self.update_good(client)


    def add_good(self, client):
        print(f'''Выберите тип товара: {self.list_product}''')
        product_type = input()

        if product_type in self.list_product:
            print('sku')
            sku = input()
            print('price')
            price = int(input())
            print('name')
            name = input()
            print('quantity')
            quantity = int(input())
            print('brand')
            brand = input()

            if product_type == 'Tshirt':
                print('size')
                size = input()
                print('color')
                color = input()
                product = TshirtProduct(sku=sku, price=price, name=name,
                                            quantity=quantity, brand=brand, tshirtsize=size, tshirtcolor=color)
            elif product_type == 'Sneakers':
                print('size')
                size = int(input())
                print('color')
                color = input()
                product = SneakersProduct(sku=sku, price=price, name=name,
                                            quantity=quantity, brand=brand, sneakerssize=size, sneakerscolor=color)

            product.Add_product(client)
        else:
            print('Не верная категория')


    def delete_good(self, client):
        print(f'''Выберите тип товара: {self.list_product}''')
        product_type = input()

        if product_type in self.list_product:

            print("Введите Sku")
            Sku = int(input())

            if product_type == 'Tshirt':
                TshirtProduct.Delete_product(client, Sku)

            elif product_type == 'Sneakers':
                SneakersProduct.Delete_product(client, Sku)
        else:
            print('Не верная категория')


    def update_good(self, client):
        print(f'''Выберите тип товара: {self.list_product}''')
        product_type = input()

        if product_type in self.list_product:

            print("Введите Sku")
            Sku = int(input())
            print("Введите поле которое хотите изменить")
            field = int(input())
            print("str или int")
            typevalue = input()
            print("Введите новое значение")
            if typevalue == 'int':
                value = int(input())
            elif typevalue == 'str':
                value = input()

            if product_type == 'Tshirt':
                TshirtProduct.Update_product(client, Sku, field, value)

            elif product_type == 'Sneakers':
                SneakersProduct.Update_product(client, Sku, field, value)
        else:
            print('Не верная категория')