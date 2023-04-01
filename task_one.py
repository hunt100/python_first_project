# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.

def get_arithmetic_series():
    first_element = int(input("Input first element: "))
    diff = int(input("Input difference of series: "))
    n = int(input("Input number of elements: "))
    for i in range(n):
        print(f"a[{i + 1}] = {first_element + i * diff}")


get_arithmetic_series()
