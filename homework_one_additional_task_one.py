# Найдите сумму цифр трехзначного числа.

num = input("Enter number: ")
digit_sum = 0

for digit in num:
    digit_sum += int(digit)

print("Sum: " + str(digit_sum))
