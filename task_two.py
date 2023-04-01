# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def print_element_index(element_list, minimum, maximum):
    for i in range(len(element_list)):
        if minimum <= element_list[i] <= maximum:
            print(i)


def fill_list(n):
    initial_list = []
    for i in range(n):
        initial_list.append(int(input(f"Write {i} element of list: ")))

    return initial_list


size = int(input("Input size of list: "))
input_list = fill_list(size)
min_number = int(input("Input min: "))
max_number = int(input("Input max: "))
print_element_index(input_list, min_number, max_number)
