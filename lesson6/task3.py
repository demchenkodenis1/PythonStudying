# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).

class Worker:
    # wage = None
    # bonus = None
    _income = {"wage": 12000, "bonus": 3000}

    def __init__(self, name, surname, position, _income):
        #не получилось оставить в словаре wage и bonus, чтобы можно, было менять значения не внутри класса
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income

class Position(Worker):
    # def __init__(self, name, surname, position, _income):
    #     super().__init__(name, surname, position, _income)
    def get_full_name(self):
        print(f'{self.name} {self.surname}')
    def get_total_income(self):
        # self.wage = wage
        # self.bonus = bonus
        print(f'{sum(self._income.values())}')

a = Position('Harry', 'Potter', 'wizard', Worker._income)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())

#не понял откуда None на выходе
