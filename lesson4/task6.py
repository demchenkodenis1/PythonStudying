# Урок4. Задача6
# Реализовать два небольших скрипта:
# ● итератор, генерирующий целые числа, начиная с указанного;
# ● итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание, что
# создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 —
# завершаем цикл. Вторым пунктом необходимо предусмотреть условие, при котором
# повторение элементов списка прекратится.

from itertools import count
from itertools import cycle

def my_count_func(start, finish):
    for el in count(start):
        if el > finish:
            break
        else:
            print(el)
def my_cycle_func(my_list, iteration):
    i = 0
    it = cycle(my_list)
    while i < iteration:
        print(next(it))
        i += 1
my_count_func(start = int(input("Введите начальное число: ")), finish = int(input("Введите конечное число: ")))
my_list = [1, 2, 3]
my_cycle_func(my_list, iteration = int(input(f"Введите предельное количество элементов при выведении списка {my_list}: ")))