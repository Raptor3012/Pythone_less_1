
class Sneakers(object):

    def __init__(self, name, count, manuf, price, size):
        """Constructor"""
        self.Name
        self.Count
        self.Manufacturer
        self.Price
        self.Size
    
class Storage(object):

    def __init__(self, listProduct = []):
        self.ListProduct = listProduct

    def AddProduct(self, product):
        self.ListProduct.append(product)

    def Print(self):
        for obj in self.ListProduct:
            print(obj.Name, obj.Count, obj.Manufacturer, obj.Price, obj.Size)

storage = Storage()

while(True):
    print("Выберете действие: '1' Добавить, '2' Покаазать склад ")
    inp = input()
    if inp == '1':
        print('Введите данные')
        inp = input().split(' ')

    elif inp == '2':
        storage.Print()