import sys

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
    
    def LoadDataFromFile(self, filepath):
        f = open(filepath, 'r')
        for line in f:
            inp = line.split(' ')
            storage.AddProduct(Sneakers(inp[0],inp[1],inp[2],inp[3],inp[4]))
        f.close()

    def SaveDataFromFile(self):
        f = open('./data/datasave.txt', 'w')
        for obj in self.ListProduct:
            f.writelines([obj.Name, ' ', obj.Count, ' ', obj.Manufacturer, ' ', obj.Price, ' ', obj.Size])
        f.close()

storage = Storage()

while(True):
    print("Выберете действие: \n'1':Добавить \n'2':Покаазать склад \n'3':Загрузить данные \n'4':Статистика \n'5':Выход ")
    inp = input()
    if inp == '1':
        print('Введите данные')
        inp = input().split(' ')
        storage.AddProduct(Sneakers(inp[0],inp[1],inp[2],inp[3],inp[4]))    
    elif inp == '2':
        storage.Print()
    elif inp == '3':
        print("Введите путь к файлу:")
        inp = input()
        storage.LoadDataFromFile(inp)
    elif inp == '4':
        storage.Print()
    elif inp == '5':
        storage.SaveDataFromFile()
        sys.exit()