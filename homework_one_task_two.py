#Пользователь вводит время в секундах.
#Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
#Используйте форматирование строк.

seconds = int(input("Write down time in seconds: "))
minutes = seconds // 60
hours = minutes // 60

str_template = f"Time in format hh:mm:ss - {hours:.1f}:{minutes:.1f}:{seconds:}"
print(str_template.format(hours, minutes, seconds))
