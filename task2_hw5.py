# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет
# количества строк, количества слов в каждой строке.
with open("file.txt", "r") as f_obj:
    content = f_obj.read()
    number_of_words = content.count(' ')
    number_of_lines = content.count('\n')
    print(number_of_words)
    print(number_of_lines)
    print(content)