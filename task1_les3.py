# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
# у пользователя, предусмотреть обработку ситуации деления на ноль.
def division_of_two_numbers(number1: float, number2: float) -> float:
    if number2 == 0:
        return 'Impossible operations - division by zero!'
    return round (number1 / number2, 2)

number1 = float(input('Enter the first number: '))
number2 = float(input('Enter the second number: '))

print( division_of_two_numbers(number1, number2))
# комментарий