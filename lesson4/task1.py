# Урок4. Задача1
# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной
# платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во
# время выполнения расчёта для конкретных значений необходимо запускать скрипт с
# параметрами.
#
from sys import argv

file_name, total_Hours, per_Hours, premium = argv
total_Hours = float(input('Введите количество отработанных часов : '))
per_Hours = float(input('Введите суммы оплаты труда за 1 час : '))
premium = float(input('Укажите размер премии: '))

def salary_calc():
    salary = ((total_Hours) * (per_Hours)) + (premium)
    return salary
print(f'Размер заработной платы составил: {salary_calc() }')
