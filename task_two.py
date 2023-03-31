# Задание 2. Подсчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры
# (4, 6 и 0) и 2 нечетные (3 и 5).
# Подсказка:
# На каждом шаге вам нужно 'доставать' из числа очередную цифру
# и смотреть является ли она четной или нечетной.
# При этом увеличиваем соответствующий счетчик
# Пока все числа не извлечены, рекурсивные вызовы продолжаем
# Условие завершения рекурсии - все числа извлечены
# Используем операции % //. Операции взятия по индексу применять нельзя.
# Решите через рекурсию. В задании нельзя применять циклы.
# Пример:
# Введите число: 123
# Количество четных и нечетных цифр в числе равно: (1, 2)

def count_digits(number, odd_counter=0, even_counter=0):
    if number == 0:
        return odd_counter, even_counter

    digit = number % 10
    if digit % 2 == 0:
        even_counter += 1
    else:
        odd_counter += 1
    return count_digits(number // 10, odd_counter, even_counter)


try:
    num = int(input("Input number: "))
except ValueError:
    print("Wrong input!")
else:
    odd, even = count_digits(num)
    print(f"In number [{num}]: Odd digits = {odd}, Even digits = {even}")
