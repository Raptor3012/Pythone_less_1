import sys
import Sneakers
import Storage


storage = Storage.Storage()
storage.LoadDataFromFile('./data/datasave.txt')

while(True):
    print("Выберете действие: \n'1':Добавить \n'2':Покаазать склад \n'3':Загрузить данные \n'4':Статистика \n'5':Выход ")
    inp = input()
    if inp == '1':
        print('Введите данные')
        inp = input().split(' ')
        storage.AddProduct(Sneakers.Sneakers(inp[0],inp[1],inp[2],inp[3],inp[4]))    
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