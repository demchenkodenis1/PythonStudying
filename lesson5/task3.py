# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('file_3.txt', 'r', encoding="utf-8") as my_file:
    highSalary = []
    lowSalary = []
    content = my_file.read()
    my_list = content.split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           lowSalary.append(i[0])
           highSalary.append(i[1])
print(f'Оклад меньше 20.000 {lowSalary}, средний оклад {sum(map(int, highSalary)) / len(highSalary)}')

