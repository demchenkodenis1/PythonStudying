# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = list()
with open('file_4.txt', 'r', encoding="utf-8") as my_list:
    for i in my_list:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]])
    print(new_file)
with open('file_4_new.txt', 'w', encoding="utf-8") as myNew_list:
    myNew_list.writelines(new_file)