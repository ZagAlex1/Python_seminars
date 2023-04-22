# Задача No33. Решение в группах
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4 Output: 1 3 3 3 1


import random

# Первый вариант

size = int(input('Введите размер списка: '))
my_list = [random.randint(1, 5) for _ in range(size)]
print(my_list)

max_element = max(my_list)
min_element = min(my_list)
index = 0

while index < len(my_list):
    if my_list[index] == max_element:
        my_list[index] = min_element
    index += 1
print(my_list)


# Второй вариант

# mark_list = [random.randint(1, 5) for _ in range(10)]
# print(mark_list)
# mark_list = [min(mark_list) if i == max(mark_list) else i for i in mark_list]
# print(mark_list)
