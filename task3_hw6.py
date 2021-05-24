# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position реализовать
# методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу
# примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    # name = ''
    # surname = ''
    # position = ''
    # _income = {'salary:', 0,'bonus:',0}


    def __init__(self, name, surname, position, income:dict):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        return (self.name, self.surname)

    def total_income(self):
        return (sum(self._income))


ivanov = Position('Ivan','Ivanov','director',{100,20})
print(ivanov.name, ivanov.surname, ivanov.position, ivanov._income)

print(ivanov.get_full_name())
print(ivanov.total_income())
