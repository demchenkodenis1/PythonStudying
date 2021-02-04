# Урок3. Задача1
# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def division():
    try:
        dividend = int(input('Введите число делимое: '))
        divider = int(input('Введите число делитель: '))
        quotient = dividend / divider
        print(f'Результат деления: {quotient}')
    except  ZeroDivisionError:
        return print('Ошибка деления на ноль!')
    return quotient
division()
