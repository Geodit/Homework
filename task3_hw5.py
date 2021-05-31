# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
with open("file.txt", "r") as f_obj:
    content = f_obj.read()
    number_of_lines = content.count('\n')
    f_obj.seek(0)
    line_content = []
    for i in range(number_of_lines):
        line_content.append(f_obj.readline())
sum = 0
for i in range(number_of_lines):
    if int(line_content[i].split()[1]) < 20000:
        print(line_content[i].split()[0])
        sum += int(line_content[i].split()[1])
print ('Average salary: ', round(sum / number_of_lines, 2))

