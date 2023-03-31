# Задание 1. Написать программу, которая будет складывать, вычитать,
# умножать или делить два числа. Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться, а должна
# запрашивать новые данные для вычислений. Завершение программы должно
# выполняться при вводе символа '0' в качестве знака операции. Если пользователь
# вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
# сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль,
# если он ввел 0 в качестве делителя.
# Подсказка:
# Вариант исполнения:
# - условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
# - условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
# Решите через рекурсию. В задании нельзя применять циклы.
# Пример:
# Введите операцию (+, -, *, / или 0 для выхода): +
# Введите первое число: 214
# Введите второе число: 234
# Ваш результат 448
# Введите операцию (+, -, *, / или 0 для выхода): -
# Введите первое число: вп
# Вы вместо трехзначного числа ввели строку (((. Исправьтесь
# Введите операцию (+, -, *, / или 0 для выхода):

def execute_calculator():
    available_operation = ["+", "-", "*", "/", "0"]
    operation = input("Input math operation (+, -, *, / or 0 to exit): ")
    if operation in available_operation:
        if operation == "0":
            return

        try:
            first_number = int(input("Input first number: "))
            second_number = int(input("Input second number: "))
        except ValueError:
            print(f"One of the params is not a number. Retry all input again")
            execute_calculator()
        else:
            if operation == "+":
                print(f"Your result: {first_number + second_number}")
                execute_calculator()
            elif operation == "-":
                print(f"Your result: {first_number - second_number}")
                execute_calculator()
            elif operation == "*":
                print(f"Your result: {first_number * second_number}")
                execute_calculator()
            else:
                try:
                    division = first_number / second_number
                except ZeroDivisionError:
                    print("Division by zero detected, retry all input again")
                    execute_calculator()
                else:
                    print(f"Your result: {division}")
                    execute_calculator()
    else:
        print(f"Unknown operation {operation}, retry all input again")
        execute_calculator()


execute_calculator()
