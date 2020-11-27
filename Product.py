

class Product(object):
    sku = None
    prise = None
    name = None
    brand = None
    quantity = None

    def __init__(self, console=False):
        if console:
            print('Введите  sku')
            self.sku = int(input())
            print('Введите  name')
            self.name = input()
            print('Введите  prise')
            self.prise = int(input())
            print('Введите  brand')
            self.brand = input()
            print('Введите  quantity')
            self.quantity = int(input())

        