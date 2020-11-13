
class Sneakers(object):

    def __init__(self, name, count, manuf, price, size):
        """Constructor"""
        self.Name = name
        self.Count = count
        self.Manufacturer = manuf
        self.Price = price
        self.Size = size
    
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
        storage.AddProduct(Sneakers(inp[0],inp[1],inp[2],inp[3],inp[4]))    
    elif inp == '2':
        storage.Print()