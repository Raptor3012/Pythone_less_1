import sys
import Sneakers
import Storage
import monga

storage = Storage.Storage()
storage.LoadDataFromFile('./data/datasave.txt')


while(True):
    print("Выберете действие: \n'1':Добавить \n'2':Покаазать склад \n'3':Загрузить данные \n'4':Статистика \n'5':Выход ")
    inp = input()
    if inp == '1':
        print('Введите данные')
        inp = input().split(' ')
        #storage.AddProduct(Sneakers.Sneakers(inp[0],inp[1],inp[2],inp[3],inp[4])) 
        monga.Add_product(inp[0],inp[1],inp[2],inp[3],inp[4])   
    elif inp == '2':
        #storage.Print()
        inp = monga.Print_data()
        for obj in inp:
            print(obj)
    elif inp == '3':
        print("Введите путь к файлу:")
        inp = input()
        #storage.LoadDataFromFile(inp)
        monga.LoadDataFromFile(inp)
    elif inp == '4':
        storage.ShowStatistic()
    elif inp == '5':
        storage.SaveDataFromFile()
    elif inp == '6':        
        sys.exit()