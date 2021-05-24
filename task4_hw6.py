# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в
# базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и
# WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return('car is moving')

    def stop(self):
        return('car has stopped')

    def turn(self):
        return('car is turning')

    def show_speed(self):
        return(self.speed)


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return(f'your speed - {self.speed}')


class SportCar(Car):

    def show_speed(self):
        if self.speed > 160:
            return(f'your speed - {self.speed}')


class WorkCar(Car):

    pass

car1 = TownCar('Car1', 80, 'blue', True)
car2 = SportCar('Car2', 280, 'yellow', True)
car3 = WorkCar('Car3', 10, 'green', False)

print(car3.show_speed())
print(car2.show_speed())
print(car1.show_speed())

print(car1.go())
print(car2.stop())
print(car3.turn())

print(car3.__dict__)
print(car2.__dict__)
