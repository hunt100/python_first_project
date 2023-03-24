# 4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
# Попробуйте решить задачу двумя способами:
# 1) используя функцию sort()
# 2) без функции sort()

def my_func(first_operand, second_operand, third_operand):
    numbers = [first_operand, second_operand, third_operand]
    numbers.sort()
    return numbers[1] + numbers[2]


def my_func_simple(first_operand, second_operand, third_operand):
    if first_operand >= third_operand and second_operand >= third_operand:
        return first_operand + second_operand
    elif first_operand > second_operand and first_operand < third_operand:
        return first_operand + third_operand
    else:
        return second_operand + third_operand

try:
    a = int(input("Input first number: "))
    b = int(input("Input second number: "))
    c = int(input("Input third number: "))
except Exception as inst:
    print(f"Unhandled exception! {inst}")
else:
    print(f"{my_func(a, b, c)}")
    print(f"{my_func_simple(a, b, c)}")
