import Sneakers
import os
class Storage(object):

    def __init__(self, listProduct = []):
        self.ListProduct = listProduct
    
    def AddProduct(self, product):
        self.ListProduct.append(product)

    #  def LoadDataFromFile(self, filepath):        
    #     if os.path.exists(filepath):
    #         f = open(filepath, 'r')
    #         for line in f:
    #             inp = line.split(' ')
    #             inp = [line.rstrip('\n') for line in inp]
    #             self.AddProduct(Sneakers.Sneakers(inp[0],inp[1],inp[2],inp[3],inp[4]))
    #         f.close()

    def Print(self):
        for obj in self.ListProduct:
            obj.PrintProduct()

    # def Print(self):
    #     for obj in self.ListProduct:
    #         print(obj.Name, obj.Count, obj.Manufacturer, obj.Price, obj.Size)
    
    # def LoadDataFromFile(self, filepath):        
    #     if os.path.exists(filepath):
    #         f = open(filepath, 'r')
    #         for line in f:
    #             inp = line.split(' ')
    #             inp = [line.rstrip('\n') for line in inp]
    #             self.AddProduct(Sneakers.Sneakers(inp[0],inp[1],inp[2],inp[3],inp[4]))
    #         f.close()

    # def SaveDataFromFile(self):
    #     f = open('./data/datasave.txt', 'w')
    #     for obj in self.ListProduct:
    #         f.writelines([obj.Name, ' ', obj.Count, ' ', obj.Manufacturer, ' ', obj.Price, ' ', obj.Size, '\n'])
    #     f.close()

    # def ShowStatistic(self):
    #     listManufact = []
        
    #     for x in self.ListProduct:
    #         if x.Manufacturer not in listManufact:
    #             listManufact.append(x.Manufacturer)
    #     listSize = []
    #     sizefrommanufact = dict.fromkeys(listManufact, [])
    #     for x in self.ListProduct:
    #         #if x.Size not in sizefrommanufact[x.Manufacturer]:
    #         sizefrommanufact[x.Manufacturer].append(x.Size)
    #         if x.Size not in listSize:
    #             listSize.append(x.Size)

    #     print("Производители:", listManufact)
    #     print("Размеры:", listSize)
    #     print(sizefrommanufact)
        