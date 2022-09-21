# Task 4 - Random book link generator
# У меня пятый вариант, доп. ограничения не предусмотрены


import csv
import random

row_count = 0


file = open('result.txt', 'w')

# Вычисляем кол-во строк в таблице и сохраняем значение в переменную
with open('books.csv', 'r', encoding='cp1251') as f:

    table = csv.reader(f, delimiter=';')
    
    for i in table:
        row_count += 1

with open('books.csv', 'r', encoding='cp1251') as f:

    table = csv.reader(f, delimiter=';')


    # Создаем массив для рандомных ID
    id_list = []

    # Сюда будем складировать записи исходя из их ID
    book_list = []

    # Наполняем массив с ID
    for i in range(20):
        id_list.append(random.randint(0, row_count))

    # Сортируем по возрастанию, чтобы наполнить book_list за один проход по таблице
    id_list = sorted(id_list)

    # Переменная для ID 
    id = 0
    # Переменная-счетчик записей для вывода (кол-во таких записей не должно превышать 20)
    count = 0
    
    for row in table:
        if id in id_list and count < 20:
            book_list.append(row)
            id_list.remove(id)
            id += 1
            count += 1
        else:
            id += 1
    

    # Выводим 20 рандомных записей
    for i in range(len(book_list)):
        file.write(str(i+1) + str(book_list[i][3]) + '. '+str(book_list[i][1]) + ' - ' + str(book_list[i][6][6:10]))
        file.write('\n')

file.close()








