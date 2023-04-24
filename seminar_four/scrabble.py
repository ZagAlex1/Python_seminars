# Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков;
# Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость
# введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое
# содержит либо только английские, либо только русские буквы.
# *Пример:*
#
# ноутбук
#     12

# Первый вариант

# scrabble = {'АВЕИНОРСТAEIOULNSTR': 1,
#             'ДКЛМПУDG': 2,
#             'БГЁЬЯBCMP': 3,
#             'ЙЫFHVWY': 4,
#             'ЖЗХЦЧK': 5,
#             'JXШЭЮ': 8,
#             'QZФЩЬ': 10}

# word = input('Введите слово: ')
# total = 0

# for letter in word.upper():
#     for letters in scrabble.keys():
#         if letter in letters:
#             total += scrabble.get(letters)
#             break
# print(total)

# Второй вариант

# scrabble = {1: 'АВЕИНОРСТAEIOULNSTR',
#             2: 'ДКЛМПУDG',
#             3: 'БГЁЬЯBCMP',
#             4: 'ЙЫFHVWY',
#             5: 'ЖЗХЦЧK',
#             8: 'JXШЭЮ',
#             10: 'QZФЩЬ'}

# for letter in word.upper():
#     for points, letters in scrabble.items():
#         if letter in letters:
#             total += points
#             break
# print(total)

# Третий вариант

# my_dict = {}
# my_dict.update(my_dict.fromkeys('АВЕИНОРСТAEIOULNSTR', 1))
# my_dict.update(my_dict.fromkeys('ДКЛМПУDG', 2))
# my_dict.update(my_dict.fromkeys('БГЁЬЯBCMP', 3))
# my_dict.update(my_dict.fromkeys('ЙЫFHVWY', 4))
# my_dict.update(my_dict.fromkeys('ЖЗХЦЧK', 5))
# my_dict.update(my_dict.fromkeys('JXШЭЮ', 8))
# my_dict.update(my_dict.fromkeys('QZФЩЬ', 10))
# print(my_dict)

# word = input('Введите слово: ')
# total = 0
# for letter in word.upper():
#     total += my_dict.get(letter)
# print(f'Слово "{word}" весит {total} баллов')

# Четвертый вариант

scrabble = [(1, 'АВЕИНОРСТAEIOULNSTR'),
            (2, 'ДКЛМПУDG'),
            (3, 'БГЁЬЯBCMP'),
            (4, 'ЙЫFHVWY'),
            (5, 'ЖЗХЦЧK'),
            (8, 'JXШЭЮ'),
            (10, 'QZФЩЬ')]

my_dict = {}
[my_dict.update(my_dict.fromkeys(values, key)) for key, values in scrabble]

word = input('Введите слово: ')
total = 0
for letter in word.upper():
    total += my_dict.get(letter)
print(f'Слово "{word}" весит {total} баллов')