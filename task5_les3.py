# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
# выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# умма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный
# символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале
# нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.пывпы

def addition(numbers:str):
    sum = 0
    for number in numbers:
        if number.isdigit():
            sum += int(number)
        else:
            return(sum)
    return(sum)

sum = 0
while True:
    numbers = input('Enter numbers separated by space and then press "Enter" to start calculations: ').split()
    sum += addition(numbers)
    print(sum)

