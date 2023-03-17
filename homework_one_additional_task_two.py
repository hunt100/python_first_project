# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

crane_sum = int(input("Enter sum of cranes: "))

if crane_sum % 6 == 0:
    result = crane_sum // 6
    print(f"For sum: {crane_sum} -> {result}, {4 * result}, {result}")
else:
    print(f"{crane_sum} cannot be divided fully between Katya, Petya and Sergey")
