from TshirtProduct import TshirtProduct
from SneakersProduct import SneakersProduct

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
            print(f'''Выберите тип товара: {self.list_product}''')
            product_type = input()

            if product_type in self.list_product:

                if product_type == 'Tshirt':
                    product = TshirtProduct(console=True)

                elif product_type == 'Sneakers':
                    product = SneakersProduct(console=True)

                product.Add_product(client)
            else:
                print('Не верная категория')

        if run_command == 'delete_good':
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

        if run_command == 'update_good':
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

