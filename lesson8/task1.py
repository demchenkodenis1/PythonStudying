# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
        try:
            0 < day <= 31
            0 < month <= 12
            0 < year
        except:
            return f'Ошибка ввода данных'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('12 - 2 - 2021')
print(today)
# print(Data.valid(32, 2, 2021))
print(today.valid(32, 2, 2021))
# print(Data.extract('11 - 11 - 2011'))
print(today.extract('12 - 2 - 2021'))
print(Data.valid(12, 20, 2021))