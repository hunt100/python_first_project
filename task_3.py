"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""

str_list = ["attribute", "класс", "функция", "type"]
for s in str_list:
    byte_arr = bytes(s, "utf-8")
    try:
        if len(s) != len(byte_arr):
            raise ValueError
    except ValueError:
        print(f"{s} - cannot be written in b's' format")
    else:
        print(f"{s} - {byte_arr}")
