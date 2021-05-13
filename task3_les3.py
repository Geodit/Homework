# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
# наибольших двух аргументов.

def my_func(number1: float, number2: float, number3: float) -> float:
    result = [ number1, number2, number3 ]
    result.sort()
    print(result[1]+result[2])

number1 = float(input('Enter the first number: '))
number2 = float(input('Enter the second number: '))
number3 = float(input('Enter the third number: '))

my_func(number1, number2, number3)