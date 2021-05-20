# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с
# прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое
# слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться
# с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def first_uppercase_character(word:str):
    return(word.title())

word = input('Enter the word in lowercase characters: ')
print(first_uppercase_character(word))

words = input('Enter the wordS in lowercase characters separated by space: ')
print(first_uppercase_character(words))

# they both work equally