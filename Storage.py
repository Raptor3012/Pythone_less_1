import Sneakers

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
            self.AddProduct(Sneakers.Sneakers(inp[0],inp[1],inp[2],inp[3],inp[4]))
        f.close()

    def SaveDataFromFile(self):
        f = open('./data/datasave.txt', 'w')
        for obj in self.ListProduct:
            f.writelines([obj.Name, ' ', obj.Count, ' ', obj.Manufacturer, ' ', obj.Price, ' ', obj.Size])
        f.close()