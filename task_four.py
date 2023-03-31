# Задание 4. Найти сумму n элементов следующего ряда чисел:
# 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.
# Пример:
# Введите количество элементов: 3
# Количество элементов - 3, их сумма - 0.75
# Решите через рекурсию. В задании нельзя применять циклы.
# Нужно обойтисть без создания массива!

def sum_of_series(element, series_sum=0, digit=1.0):
    series_common_coefficient = -2
    if element == 0:
        return series_sum

    series_sum += digit
    return sum_of_series(element - 1, series_sum, digit / series_common_coefficient)


n = int(input("Input number of elements: "))
print(f"Number of elements - {n}, its sum: {sum_of_series(n)}")
