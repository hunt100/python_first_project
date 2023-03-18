# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Input n: "))
i = 1
result = 1
while result <= n:
    print(result)
    result = 2 ** i
    i += 1
