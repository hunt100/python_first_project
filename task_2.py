"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

str_list = ["class", "function", "method"]
for s in str_list:
    byte_arr = bytes(s, "utf-8")
    print(f"{s} - {byte_arr} - {type(byte_arr)}")
    print(f"Byte array length: {len(byte_arr)}")
    for byte in byte_arr:
        print(byte, end=" ")
    print("\n")
