# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко
# он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм
# есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения
# одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке
# и “Пам парам”, если с ритмом все не в порядке
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам

def get_rhyme_str(initial_str):
    vowels = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
    words = initial_str.split()
    number_of_syllables_in_each_word = list()

    for item in words:
        number_of_syllables_per_word = 0
        for letter in item:
            if letter in vowels:
                number_of_syllables_per_word += 1
        number_of_syllables_in_each_word.append(number_of_syllables_per_word)

    if len(set(number_of_syllables_in_each_word)) == 1:
        print('Парам пам-пам')
    else:
        print('Пам парам')


initial_rhyme_str = input("Input rhyme str: ")
get_rhyme_str(initial_rhyme_str)
