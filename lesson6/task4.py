# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
    def go(self):
        print("машина поехала")
    def stop(self):
        print("машина остановилась")
    def turn(self, leftRight):
        print(f"машина повернула {leftRight}")

    def show_speed(self, speed):
        print(f"текущая скорость автомобиля {speed} км/ч")

class TownCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

    def show_speed(self, speed):
        if self.speed > 60:
            print(f"текущая скорость автомобиля {speed}км/ч, это выше 60 км/ч")


class SportCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)


class WorkCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

    def show_speed(self, speed):
        if self.speed > 40:
            print(f"текущая скорость автомобиля {speed}км/ч, это выше 40 км/ч")


class PoliceCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

    def police(self, is_police):
        if self.is_police:
            print(f'{self.name} машина полиции')
        else:
            print(f'{self.name} не является машиной полиции')

toyota = Car('toyota', 60, 'black', True)
print(toyota.name, toyota.speed, toyota.color, toyota.is_police)
print(toyota.go(), toyota.turn('направо'), toyota.stop(), toyota.show_speed(60))
audi = TownCar('audi', 70, 'red', True)
audi.show_speed(70)
reno = PoliceCar('reno', 60, 'white', True)
reno.police(True)
