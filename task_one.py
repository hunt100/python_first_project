# 1. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите два варианта решения: через list и через dict.
#
# Пример:
# Введите номер месяца: 10
# Результат через список: Осень
# Результат через словарь: Осень

def get_season_by_month(month_number):
    season_list = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
    if month_number in season_list[0]:
        return "Winter"
    elif month_number in season_list[1]:
        return "Spring"
    elif month_number in season_list[2]:
        return "Summer"
    elif month_number in season_list[3]:
        return "Autumn"
    else:
        return "There is no such season for month number: " + str(month_number)


def get_season_by_month_dictionary(month_number):
    if month_number < 1 or month_number > 12:
        return "There is no such season for month number: " + str(month_number)

    season_dictionary = {12: "Winter",
                         1: "Winter",
                         2: "Winter",
                         3: "Spring",
                         4: "Spring",
                         5: "Spring",
                         6: "Summer",
                         7: "Summer",
                         8: "Summer",
                         9: "Autumn",
                         10: "Autumn",
                         11: "Autumn"}

    return season_dictionary.get(month_number)


m = int(input("Write month number (1 - 12):"))
print(get_season_by_month(m))
print(get_season_by_month_dictionary(m))
