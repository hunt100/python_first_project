#Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

ticket_num = input("Enter ticket number: ")

first_part_sum = 0
for digit in ticket_num[:3]:
    first_part_sum += int(digit)

second_part_sum = 0
for digit in ticket_num[3:]:
    second_part_sum += int(digit)

is_lucky_text = "YES" if first_part_sum == second_part_sum else "NO"
print(f"ticket number: {ticket_num} -> {is_lucky_text}")
