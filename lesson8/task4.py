# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

class Storage:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)


    def extract(self):
        name1 = input("Введите имя для удаления из списка")


        # if name1 in self._dict:     удаляет целый тип Scaner, Printer, Xerox
        #     del self._dict[name1]
        #удаляет последний введенный объект из типа Scaner, Printer, Xerox
        if self._dict:
            self._dict.setdefault(name1).pop()

class Equipment:
    def __init__(self, name, isn, year):
        self.name = name
        self.isn = isn
        self.year = year
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.isn} {self.year}'

class Printer(Equipment):
    def __init__(self, series, name, isn, year):
        super().__init__(name, isn, year)
        self.series = series

    def __repr__(self):
        return f'{self.name} {self.series} {self.isn} {self.year}'

    def action(self):
        return 'Печатает'

class Scaner(Equipment):
    def __init__(self, name, isn, year):
        super().__init__(name, isn, year)

    def action(self):
        return 'Сканирует'

class Copier(Equipment):
    def __init__(self, name, isn, year):
        super().__init__(name, isn, year)

    def action(self):
        return 'Копирует'


storage = Storage()
scaner = Scaner('canon', '458552', 2001)
storage.add_to(scaner)
scaner = Scaner('hp', '998557', 2004)
storage.add_to(scaner)
scaner = Scaner('panasonic', 78854787, 2006)
storage.add_to(scaner)
printer = Printer('e-320', 'sony', '8554745', 2018)
storage.add_to(printer)
printer = Printer('M-800', 'sony', '77511', 2021)
storage.add_to(printer)
copier = Copier('xerox', '6585478', 2020)
storage.add_to(copier)
print(storage._dict)
storage.extract()
print()
print(storage._dict)
