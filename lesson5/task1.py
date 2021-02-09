# Урок5. Задача1
# Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
# строка.

my_list = list()
while True:
    data = input("Введите данные: ")
    if data == '':
        print(my_list)
        break
    else:
        data += '\n'
        my_list.append(data)

    fp = open("file_1.txt", "w", encoding="utf-8")
    fp.writelines(my_list)
