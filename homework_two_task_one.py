#  На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
#  Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
#  Выведите минимальное количество монет, которые нужно перевернуть (пользователь говорит как она лежит)

n = int(input("Input number of coins: "))
count_tails = 0
count_eagles = 0
for i in range(n):
    coin = int(input("Is this coin eagle(1) or tails(0)? "))
    if coin == 0:
        count_tails += 1
    else:
        count_eagles += 1

if count_eagles > count_tails:
    print(f"Min to turnover: {count_tails}")
else:
    print(f"Min to turnover: {count_eagles}")
