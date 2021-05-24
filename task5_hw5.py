# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import random
with open("file3.txt","w+") as f_obj:
    while True:
        a = str(random.randint(1,20))
        print(a)
        f_obj.write(a)
        f_obj.seek(0)
        content = f_obj.read()
        print(sum([int(i) for i in content.split(' ')]))

        if input('Enter "q" for exit or "Enter" to continue generating ') == 'q':
            break

        f_obj.write(' ')