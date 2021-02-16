# Урок3. Задача2
# Выполнить функцию, которая принимает несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
# должна принимать параметры как именованные аргументы. Осуществить вывод данных о
# пользователе одной строкой.

name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')
dateOfBirth = input('Введите дату вашего рождения: ')
city = input('Введите место вашего рождения: ')
email = input('Введите ваш email: ')
telephoneNumb = input('Введите ваш номер телефона: ')


def dataUser(name, surname, dateOfBirth, city, email, telephoneNumb):
    return ' '.join([name, surname, dateOfBirth, city, email, telephoneNumb])
print(dataUser(name, surname, dateOfBirth, city, email, telephoneNumb))
