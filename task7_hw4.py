# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
#     Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.


# 7a)
# def my_func(n):
#     for i in range(n):
#         yield i
#
# for i in my_func(5):
#     print(i)

# 7b)

def my_func(n):
    a = n
    if n == 1:
        return n
    else:
        a = n - 1
        yield a
        return n*my_func(n-1)


for i in my_func(5):
    print(i)
# print(my_func(5))

# не понял, как сделать втоую часть