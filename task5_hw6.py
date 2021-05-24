# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
# draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить
# уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return ('Drawing is starting')


class Pen(Stationery):

    def draw(self):
        return ('Drawing is starting1')


class Pencil(Stationery):

    def draw(self):
        return ('Drawing is starting2')


class Handle(Stationery):

    def draw(self):
        return ('Drawing is starting3')


pen1 = Pen('pen1')
pen2 = Pen('pen2')

pencil1 = Pencil('pencil1')
handle1 = Handle('handle1')

print(pen1.draw())
print(pen2.draw())

print(pencil1.draw())
print(handle1.draw())