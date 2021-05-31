# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным.
#     Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
#     Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
from sys import argv

script_name, first_number, characters = argv

print("Имя скрипта: ", script_name)
print("The first number of sequence: ", first_number)
print("The list of characters: ", characters)

from itertools import cycle
my_list = [i for i in range(int(first_number), int(first_number) + 11)]
for el in cycle(my_list):
    if el == int(first_number)+10:
        break
    print(el)

# вторую часть задания не понял, как определить список??