# Additional task 1 - Tags

import csv

with open('books.csv', 'r', encoding='cp1251') as f:

    table = csv.reader(f, delimiter=';')

    # Создаем массив, куда будем добавлять теги
    tags_list = []

    for row in table:

        # Создаем временный массив
        tags_temp = row[12].split('#')[1:]

        for tag in tags_temp:
            # Отбираем уникальные теги из временного массива в основной
            if not tag in tags_list:
                tags_list.append(tag)
                
        # Очищаем временный массив
        tags_temp = []

    print('Перечнь всех тегов:')

    for tag in tags_list:
        if tag.startswith(' '):
            print(tag[1:].capitalize())
        else:
            print(tag.capitalize())

    # Проверка уникальности каждого тега
    # for i in tags_list:
    #     print(tags_list.count(i))









