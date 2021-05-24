# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
# на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
# и завершать скрипт.

class TrafficLight:
    __colour = ('red', 'yellow', 'green')
    __delay = (10, 5,20)
    __count = -1

    def __init__(self, name):
        self.name = name

    def running(self):
        TrafficLight.__count += 1
        if TrafficLight.__count == 3:
            TrafficLight.__count = 0
        return (TrafficLight.__colour[TrafficLight.__count])

    def delay(self):
        import time
        time.sleep(TrafficLight.__delay[TrafficLight.__count])


example = TrafficLight('example')

while True:
    print(example.running())
    example.delay()
    print(example.running())
    example.delay()
    print(example.running())
    example.delay()

