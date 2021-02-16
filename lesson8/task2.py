# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
# в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroDivisionError:
    def __init__(self, dividend, divider):
        self.divider = dividend
        self.denominator = divider

    @staticmethod
    def division(dividend, divider):
        try:
            return print(f'{dividend / divider}')
        except:
            return print(f"Ошибка деления на ноль")

div = ZeroDivisionError(6, 2)
ZeroDivisionError.division(1, 0)
ZeroDivisionError.division(6, 2)
div.division(1, 0)
