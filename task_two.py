# 2. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль (try except).
#
# Пример:
# Введите первое число: 10
# Введите второе число: 0
# Вы что? Пытаетесь делить на 0!
#
# Process finished with exit code 0
#
# Пример:
# Введите первое число: 10
# Введите второе число: 10
# 1.0
#
# Process finished with exit code 0

def division(first_operand, second_operand):
    return first_operand / second_operand


try:
    a = int(input("First number: "))
    b = int(input("Second number: "))
    division(a, b)
except ZeroDivisionError as inst:
    print(f"Division by zero exception! [{inst}]")
except Exception as inst:
    print(f"Unhandled exception! {inst}")
else:
    print(f"{a} / {b} = {division(a, b)}")
