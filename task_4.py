"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
str_list = ["attribute", "класс", "функция", "type"]
for s in str_list:
    encoded_byte_arr = s.encode("utf-8")
    print(f"{s} in encoded format: {encoded_byte_arr}")
    decoded_str = encoded_byte_arr.decode("utf-8")
    print(f"{encoded_byte_arr} decoded to: {decoded_str}\n")
