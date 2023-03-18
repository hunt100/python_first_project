#Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

import math

sum_for_prediction = int(input("Input sum of x and y: "))
multiply_for_prediction = int(input("Input multiplication of x and y: "))

# x**2 - sum * x + multiplication = 0
determinant = sum_for_prediction ** 2 - 4 * multiply_for_prediction
x = (sum_for_prediction + math.sqrt(determinant)) / 2
y = (sum_for_prediction - math.sqrt(determinant)) / 2

print(f"For S = {sum_for_prediction}, P = {multiply_for_prediction} -> {x}, {y}")
