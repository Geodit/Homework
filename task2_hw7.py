# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
# одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
# одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы
# для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC,abstractmethod

class Clothes(ABC):
    def __init__(self, name, size):
        self.size = size
        self.name = name

    @property
    @abstractmethod
    def raw_material(self):
        pass

    def __add__(self, other):
        return(self.raw_material + other.raw_material)


class Coat(Clothes):

    @property
    def raw_material(self):
        return(self.size / 6.5 + 0.5)


class Suit(Clothes):

    @property
    def raw_material(self):
        return(self.size * 2 + 0.3)


suit1 = Suit('suit1', 150)
coat1 = Coat('coat1', 48)

print(suit1 + coat1)
