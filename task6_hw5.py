# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
# наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для
# каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
my_dict = {}
with open("file4.txt", "r") as f_obj, open("file5.txt", "w") as f_obj2:
    content = f_obj.read().split('\n')
    for i in content:
        my_sum = 0
        for j in (i.partition(':')[2].split(' ')):
            l = ''
            for k in j:
                if k.isdigit():
                    l += k
            if l != '':
                my_sum += int(l)
        f_obj2.writelines(i.partition(':')[0] + ': ' + str(my_sum) + '\n')

# здесь ничего другого не придумал, к сожалению.. торопился к началу урока
