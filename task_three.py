# 3. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
#
# Пример:
# Иван Иванов 1846 года рождения, проживает в городе Москва,
# email: jackie@gmail.com, телефон: 01005321456

#Что-то я не совсем понимаю, как здесь можно массивы применить, если можно напрямую сделать 🤔🤔🤔
def initialize_user(name, surname, birth_year, birth_city, email, phone):
    print(f"{name} {surname} {birth_year} year of birth, live in {birth_city} city, "
          f"email: {email}, phone: {phone}")


try:
    name = input('Input name: ')
    surname = input('Input surname: ')
    year_of_birth = int(input('Input year_of_birth: '))
    city = input('Input city: ')
    email = input('Input email: ')
    phone = input('Input phone: ')
except Exception as inst:
    print(f"Unhandled exception! {inst}")
else:
    initialize_user(name, surname, year_of_birth, city, email, phone)
