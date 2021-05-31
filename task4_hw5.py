# . Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом
# английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
my_list = ('Один','Два','Три','Четыре')
with open("file.txt","r") as f_obj, open('file2.txt','w') as f_obj2:
    content = f_obj.read()
    number_of_lines = content.count('\n')
    f_obj.seek(0)
    for i in range(number_of_lines + 1):
        line = f_obj.readline()
        print(my_list[i] + ' - ' + line.split(' ')[2])
        f_obj2.writelines(my_list[i] + ' - ' + line.split(' ')[2])

