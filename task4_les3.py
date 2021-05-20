# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать
# в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа
# в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def exponentation(number: float, exponent: int):
    '''this function does something'''
    print (1 / number ** exponent)
    result = 1 / number
    for i in range(1, exponent):
        result /= number
    print(result)

number = float(input('Enter a positive float number: '))
exponent = int(input('Enter a negative exponent: '))
exponentation(number, exponent*(-1))
