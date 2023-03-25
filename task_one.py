# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются
# в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы
# множеств.

n = int(input("Number of elements in first set: "))
m = int(input("Number of elements in second set: "))
set_1 = set()
set_2 = set()

for idx in range(n):
    set_1.add(input(f"Write first set elements {idx}: "))

for idx in range(m):
    set_2.add(input(f"Write second set elements {idx}: "))

combine_set = set_1 & set_2
result_list = list(combine_set)
result_list.sort()
for i in result_list:
    print(i)
