# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
with open("file.txt", "w+") as f_obj:
    while (a:=input('Enter data: ')) != '':
        f_obj.write(a + '\n')
        f_obj.seek(0)
        content = f_obj.read()
        print(content)

