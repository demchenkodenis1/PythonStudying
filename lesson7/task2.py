# Урок7. Задание2
# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class textil:
    def __init__(self, V, H):
        self.V = V
        self.H = H

    def coatQuantity(self):
        return self.V / 6.5 + 0.5

    def suitQuantity(self):
        return self.H * 2 + 0.3

    @property
    def quantityFull(self):
        return str(f'общее количество ткани \n'
                   f' {(self.V / 6.5 + 0.5) + (self.H * 2 + 0.3)}')

class coat(textil):
    def __init__(self, V, H):
        super().__init__(V, H)
        self.coatQ = round(self.V / 6.5 + 0.5)

    def __str__(self):
        return f'количество ткани на пальто {self.coatQ}'

class suit(textil):
    def __init__(self, V, H):
        super().__init__(V, H)
        self.suitQ = round(self.H * 2 + 0.3)

    def __str__(self):
        return f'количество ткани на костюм {self.suitQ}'

coat = coat(10, 0)
suit = suit(0, 4)
print(coat)
print(suit)
print(coat.quantityFull)
print(suit.quantityFull)
print(suit.coatQuantity())
print(suit.suitQuantity())