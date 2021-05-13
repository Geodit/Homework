# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def print_user_information(name: str, surname: str,  year_of_birth: int, city: str, e_mail: str, phone: str):
    print(f'Name: {name}, surname: {surname}, year_of_birth: {year_of_birth},\ncity: {city}, e-mail: {e_mail}, phone: {phone}')

print_user_information(year_of_birth = 1990, city = 'Saratov', name = 'Igor', surname = 'Ivanov',
                       e_mail = 'ivanov@ivanov.ru', phone = '+79999999999')