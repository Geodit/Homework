# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, output_hours, rate_an_hour, bonus = argv

print("Имя скрипта: ", script_name)
print("Выработка в часах: ", output_hours)
print("Ставка в час: ", rate_an_hour)
print("Премия: ", bonus)

print('Salary is: ', int(output_hours) * int(rate_an_hour) + int(bonus))